//
//  RestaurantCell.swift
//  PraticeTableView1
//
//  Created by Subodh Sah on 1/22/24.
//

import UIKit

class RestaurantCell: UITableViewCell {
    
    @IBOutlet weak var titleLabel: UILabel!
    
    @IBOutlet weak var descriptionLabel: UILabel!
    
    
    static let identifier = "RestaurantCell"
    
    static func nib() -> UINib {
        return UINib(nibName: "RestaurantCell", bundle: nil)
    }

    override func awakeFromNib() {
        super.awakeFromNib()
        
    }
    
    func configureCell(_ title: String,_ description: String) {
        self.titleLabel.text = title
        self.descriptionLabel.text = description
    }
    
}
