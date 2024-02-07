//
//  Model.swift
//  PraticeTableView
//
//  Created by Subodh Sah on 1/20/24.
//

import Foundation

struct Restaurant: Codable, Equatable {
    
    var status: String
    var description: String
    var deliveryFee: Int
    var coverImgUrl: String
    var id: Int
    var name: String
    
    enum CodingKeys: String, CodingKey {
        case status
        case description
        case deliveryFee = "delivery_fee"
        case coverImgUrl = "cover_img_url"
        case id
        case name
    }
    
}
