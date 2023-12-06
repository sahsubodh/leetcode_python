import UIKit
 
/*
# PROMPT:
Today, we're going to have you implement a simple image manager class for a small application. The image
 manager class, given a URL, is responsible for fetching an image over the network and caching the image
in memory to prevent repeated network requests for the same resource (URL).
 
We have provided you the skeleton ImageManager class and a single public fetchImage method stub. Your job
 is to implement this method and return a decoded UIImage or an Error to a completion handler. You may add
additional instance variables and methods to the class.
 
Perfect Swift syntax is not expected nor are API method signatures to Apple frameworks. Please feel free
 to ask any clarifying questions throughout the exercise.
 
 1) download image
 2) nscache <string, image>
 3) errors downloading image - handle that using enums
 4) place holder image
*/

// cache is used by a single file
class ImageCache {
    
//    static var instance = ImageCache()
        
    init() {
        
    }
    
    var imageDictionary: NSCache<NSString, UIImage> = NSCache()
    
    func addToCache(_ image: UIImage, _ url : NSString) {
        
        imageDictionary.setObject(image, forKey: url)
    }
    
    func checkCache(url: NSString) -> UIImage? {
        
        if let imageFromCache = imageDictionary.object(forKey: url){
            return imageFromCache
        }
        
        return nil
    }
    
}

enum ImageDownloadError: Error {
    case invalidURL
    case corruptedData
    case decodeFailure
}

 
/// An object that retrieves images from a remote source and caches them in memory.
@available(iOS 15.0, *)
public class ImageManager {
    
    var cache: ImageCache
    
    init(cache: ImageCache) {
        self.cache = cache
    }
 
    /// Fetches an image from a remote source.
    ///
    /// - Parameters:
    ///   - url: The URL of the image.
    ///   - completionHandler: The result of the fetch.
    public func fetchImage(for url: URL, completionHandler: @escaping (Result<UIImage, Error>) -> Void) {
        
        //check if image is already in cache if so load it
        if let imageFromCache = cache.checkCache(url: url.absoluteString as NSString) {
            completionHandler(.success(imageFromCache))
              return
        }
        
        let task = URLSession.shared.dataTask(with: URLRequest(url: url)) { [weak self] data, response, error in
            
            guard let self else {
                completionHandler(.failure(ImageDownloadError.invalidURL))
                return
            }
            
            if let error = error {
                completionHandler(.failure(ImageDownloadError.invalidURL))
                return
            }
            
            guard let httpURLResponse = response as? HTTPURLResponse,
                        httpURLResponse.statusCode == 200,
                        let data = data else {
                completionHandler(.failure(ImageDownloadError.corruptedData))
                      return
                  }
            
            if let image = UIImage(data: data) {
                cache.addToCache(image, url.absoluteString as NSString)
                completionHandler(.success(image))
                return
            } else {
                completionHandler(.failure(ImageDownloadError.corruptedData))
                return
            }
        }
        task.resume()
    }
}
 
// Call Site
let testImage = URL(string: "https://picsum.photos/200")!
let cache = ImageCache()

let manager = ImageManager(cache: cache)

manager.fetchImage(for: testImage) { result in
    do {
        let image = try result.get()
    } catch {
        print(error)
    }
}



