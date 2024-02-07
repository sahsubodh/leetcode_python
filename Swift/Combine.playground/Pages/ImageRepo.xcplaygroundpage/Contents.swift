//: [Previous](@previous)

import Foundation
import Combine

var greeting = "Hello, playground"

let imageCache = NSCache<NSString, UIImage>()

extension UIImageView {
    @discardableResult
    func loadImageFromUrl(urlString: String, placeholder: UIImage? = nil) -> URLSessionDataTask? {
        self.image = nil
        
        let key = NSString(string: urlString)
        if let cachedImage = imageCache.object(forKey: key) {
            self.image = cachedImage
            return nil
        }
        
        if let placeholder = placeholder {
            self.image = placeholder
        }
        
        let task = URLSession.shared.dataTask(with: urlString) { data, _, _ in
            DispatchQueue.main.async {
                if let data = data,
                    let downloadedImage = UIImage(data) {
                    imageCache.setObject(downloadedImage, forKey: NSString(string: urlString))
                    self.image = downloadedImage
                }
            }
            
        }
        task.resume()
    }
}

//https://levelup.gitconnected.com/image-caching-with-urlcache-4eca5afb543a

protocol ImageRepositoryProtocol {
    func getImage(imageURL: URL) -> Future<UIImage, Error>
    func downloadImage(imageURL: URL) -> Future<UIImage, Error>
    func loadImageFromCache(imageURL: URL) -> Future<UIImage, Error>
}

/*
 https://medium.com/@master13sust/to-nscache-or-not-to-nscache-what-is-the-urlcache-35a0c3b02598
 class APIService: ServiceProtocol {
     func get( url: URL, callback: @escaping (_ data: Data?, _ error: Error?) -> Void ) {
         let request = URLRequest(url: url, cachePolicy: .returnCacheDataElseLoad, timeoutInterval: 30)
         URLSession.shared.dataTask(with: request) { (data, _, error) in
             callback(data, error)
             }.resume()
     }
 
 URLCache.shared = {
     let cacheDirectory = (NSSearchPathForDirectoriesInDomains(.cachesDirectory, .userDomainMask, true)[0] as String).appendingFormat("/\(Bundle.main.bundleIdentifier ?? "cache")/" )

     return URLCache(memoryCapacity: /*your_desired_memory_cache_size*/,
                     diskCapacity: /*your_desired_disk_cache_size*/,
                     diskPath: cacheDirectory)
 }()
 */

public class ImageRepository : ImageRepositoryProtocol {
    
    let cache = URLCache.shared
    
    func getImage(imageURL: URL) -> Future<UIImage, Error> {
        let request = URLRequest(url: imageURl)
    
        if let _ = self.cache.cachedResponse(for: request) {
            return self.loadImageFromCache(imageURL: imageURL)
        } else {
            return self.downloadImage(imageURL: imageURL)
        }
    }
    
    func downloadImage(imageURL: URL) -> Future<UIImage, Error> {
        return Future { promise in
            let request = URLRequest(url: imageURL)
            
            URLSession.shared.dataTask(with: request) { data, response, error in
                if let error = error {
                    DispatchQueue.main.async {
                        promise(.failure(error))
                    }
                } else if let data = data {
                    DispatchQueue.global().async {
                        let cachedData = CachedURLResponse(response: response!, data: data)
                        self.cache.storeCachedResponse(cachedData, for: request)

                        DispatchQueue.main.async {
                            if let image = UIImage(data: data) {
                                promise(.success(image))
                            } else {
                                promise(.failure(URLError(.badServerResponse)))
                            }
                        }
                    }
                } else {
                    DispatchQueue.main.async {
                        promise(.failure(URLError(.badServerResponse)))
                    }
                }
            }.resume()
        }
    }
    
    func loadImageFromCache(imageURL: URL) -> Future<UIImage, Error> {
        return Future { promise in
            let request = URLRequest(url: imageURL)
            
            if let data = self.cache.cachedResponse(for: request)?.data, let image = UIImage(data: data) {
                promise(.success(image))
            } else {
                promise(.failure(URLError(.cannotLoadFromNetwork)))
            }
        }
    }
    
}




//infinite scroll
/*
 func scrollViewDidScroll(_ scrollView: UIScrollView) {
     let offsetY = scrollView.contentOffset.y
     let contentHeight = scrollView.contentSize.height
     if offsetY > contentHeight - scrollView.frame.height {
         // The user has scrolled to the bottom of the table view.
         // Load more data here.
         loadMoreData()
     }
 }
 func loadMoreData() {
     // Load more data here and append it to your existing data source.
     let newData = fetchNextBatchOfData()
     dataSource.append(contentsOf: newData)
     // Reload the table view with the updated data source.
     tableView.reloadData()
 }
 */


func incrementNumber() {
    var num: Int = 5
    
    let workItem = DispatchWorkItem {
        num += 5
    }
    
    
    workItem.notify(queue: .main) {
        print("the num is \(num)")
    }
    
    let queue = DispatchQueue.global(qos: .utility)
    queue.async(execute: workItem)
}

incrementNumber()


func customFilter<T>(_ array: [T], _ isIncluded: (T) -> Bool) -> [T] {
    var result:[T] = []
    
    for element in array {
        if isIncluded(element) {
            result.append(element)
        }
    }
    
    return result
}


func swapTwoValues<T>(_ a: inout T,_ b: inout T) {
    let temp = a
    a = b
    b = temp
    
}
var x = 5
var y = 10
swapTwoValues(&x, &y)


@available(iOS 15.0, *)
public class ImageManager {

    public func fetchImage(for url: URL, completionHandler: @escaping (Result<UIImage, Error>) -> Void) {
        let request = URLRequest(url: url)

        // Check if the image is already cached
        if let cachedResponse = URLCache.shared.cachedResponse(for: request),
           let image = UIImage(data: cachedResponse.data) {
            completionHandler(.success(image))
            return
        }

        // If not cached, fetch the image from the network
        let task = URLSession.shared.dataTask(with: request) { data, response, error in
            // Handle errors
            if let error = error {
                completionHandler(.failure(error))
                return
            }

            // Decode the image data and cache it
            guard let data = data, let response = response, let image = UIImage(data: data) else {
                completionHandler(.failure(URLError(.badServerResponse)))
                return
            }

            let cachedData = CachedURLResponse(response: response, data: data)
            URLCache.shared.storeCachedResponse(cachedData, for: request)

            // Return the image
            completionHandler(.success(image))
        }

        task.resume()
    }
}

// Call Site
let testImage = URL(string: "https://picsum.photos/200")!
let manager = ImageManager()

manager.fetchImage(for: testImage) { result in
    switch result {
    case .success(let image):
        // Use the image here
        print("Image fetched successfully")
    case .failure(let error):
        // Handle error here
        print(error)
    }
}


protocol ImageCaching {
    func getCachedImage(for request: URLRequest) -> UIImage?
    func cacheImage(_ image: UIImage, for request: URLRequest)
}

class ImageCacheManager: ImageCaching {
    func getCachedImage(for request: URLRequest) -> UIImage? {
        if let cachedResponse = URLCache.shared.cachedResponse(for: request) {
            return UIImage(data: cachedResponse.data)
        }
        return nil
    }

    func cacheImage(_ image: UIImage, for request: URLRequest) {
        guard let data = image.pngData() else { return }
        let response = CachedURLResponse(response: URLResponse(), data: data)
        URLCache.shared.storeCachedResponse(response, for: request)
    }
}

@available(iOS 15.0, *)
public class ImageManager {

    private let cacheManager: ImageCaching

    init(cacheManager: ImageCaching = ImageCacheManager()) {
        self.cacheManager = cacheManager
    }

    public func fetchImage(for url: URL, completionHandler: @escaping (Result<UIImage, Error>) -> Void) {
        let request = URLRequest(url: url)

        // Check if the image is already cached
        if let cachedImage = cacheManager.getCachedImage(for: request) {
            completionHandler(.success(cachedImage))
            return
        }

        // If not cached, fetch the image from the network
        let task = URLSession.shared.dataTask(with: request) { [weak self] data, response, error in
            // Handle errors
            if let error = error {
                completionHandler(.failure(error))
                return
            }

            // Decode the image data and cache it
            guard let data = data, let image = UIImage(data: data) else {
                completionHandler(.failure(URLError(.badServerResponse)))
                return
            }

            self?.cacheManager.cacheImage(image, for: request)

            // Return the image
            completionHandler(.success(image))
        }

        task.resume()
    }
}

