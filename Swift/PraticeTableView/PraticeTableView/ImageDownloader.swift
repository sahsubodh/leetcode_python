//
//  ImageDownloader.swift
//  PraticeTableView
//
//  Created by Subodh Sah on 1/22/24.
//

import Foundation
import UIKit
import Combine


protocol ImageDownloading {
    func downloadImage(for url: URL, completion: @escaping(UIImage?) -> Void)
}

protocol ImageDownloading1 {
    func downloadImage(for url: URL, completion: @escaping (UIImage?) -> Void)
}

class ImageDownloader1: ImageDownloading1 {
    
    private var cancellables = Set<AnyCancellable>()
    private var cache = NSCache<NSString, UIImage>()
    
    func downloadImage(for url: URL, completion: @escaping (UIImage?) -> Void) {
        
        URLSession.shared.dataTaskPublisher(for: url)
            .map {UIImage(data: $0.data)}
            .receive(on: DispatchQueue.main)
            .replaceError(with: UIImage(named: "person"))
            .sink{ [weak self] image in
                if let image = image  {
                    self?.cache.setObject(image, forKey: url.absoluteString as NSString)
                }
                completion(image)
            }.store(in: &cancellables)
    }
    
    

    
}

class ImageDownloader: ImageDownloading {
    
    private var cancellables = Set<AnyCancellable>()
    private var cache = NSCache<NSString, UIImage>()
    
    func downloadImage(for url: URL, completion: @escaping (UIImage?) -> Void) {
        
        if let cachedImage = self.cache.object(forKey: url.absoluteString as NSString) {
            completion(cachedImage)
            return
        }
        
        URLSession.shared.dataTaskPublisher(for: url)
            .map { UIImage(data: $0.data) }
            .replaceError(with: UIImage(named: "person"))
            .receive(on: DispatchQueue.main)
            .sink{ [weak self] image in
                if let image = image {
                    self?.cache.setObject(image, forKey: url.absoluteString as NSString)
                }
                completion(image)
            }
//        
//            .sink { [weak self] image in
//                       if let image = image {
//                           self?.cache.setObject(image, forKey: url.absoluteString as NSString)
//                       }
//                       completion(image)
//                   }
            .store(in: &cancellables)
            
        
        
    }
    
    
}



