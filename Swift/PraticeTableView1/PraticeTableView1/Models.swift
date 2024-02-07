//
//  Models.swift
//  PraticeTableView1
//
//  Created by Subodh Sah on 1/22/24.
//

import Foundation

/*
 {
    "status":"Closed",
    "description":"Burgers, Fast Food, Fries, Sandwiches, American, Late Night, Lunch, Comfort Food, Dinner, Comfort, Chicken, Sandwich, Vegetarian, Gluten-Free, Free Delivery, Pasta, Soup, &Drinks, Cheesesteaks, Deals, Dessert, Dinners, Good for Groups, Pickup, Restaurants, Salads, Soda, Alcohol",
    "delivery_fee":100,
    "cover_img_url":"https://cdn.doordash.com/media/restaurant/cover/The-Melt.png",
    "id":62087,
    "name":"The Melt"
 },
 */


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
