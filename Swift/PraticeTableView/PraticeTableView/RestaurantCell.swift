//
//  RestaurantCell.swift
//  PraticeTableView
//
//  Created by Subodh Sah on 1/20/24.
//

import UIKit

class CellViewModel {
    let title: String
    let description: String

    init(title: String, description: String) {
        self.title = title
        self.description = description
    }
}

class RestaurantCell: UITableViewCell {
    
    static let identifier = "RestaurantCell"
    
    static func nib() -> UINib {
        return UINib(nibName: "RestaurantCell", bundle: nil)
    }

    @IBOutlet weak var titleLabel: UILabel!
    @IBOutlet weak var descriptionLabel: UILabel!
    
    override func awakeFromNib() {
        super.awakeFromNib()
     
    }
    
    func setFields(_ title: String = "", description: String = "") {
        self.titleLabel.text = title
        self.descriptionLabel.text = description
    }

    override func setSelected(_ selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)
    }
    
}
