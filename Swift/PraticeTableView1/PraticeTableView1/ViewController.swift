//
//  ViewController.swift
//  PraticeTableView1
//
//  Created by Subodh Sah on 1/22/24.
//

import UIKit
import Combine


class ViewController: UIViewController, UITableViewDelegate, UITableViewDataSource {
    
    @IBOutlet weak var tableView: UITableView!
    
    var viewModel: RestaurantViewModel?
    var cancellables = Set<AnyCancellable>()
    

    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.title = "Pratice"
//        self.navigationItem.title = "Pratice"

        
        viewModel = RestaurantViewModel(networkService: NetworkService())
        
        self.tableView.register(RestaurantCell.nib(), forCellReuseIdentifier: RestaurantCell.identifier)
        self.tableView.delegate = self
        self.tableView.dataSource = self
        
        if let vm = viewModel {
            vm.fetchRestaurants()
        }
        
        viewModel?.$resturants.sink(receiveValue: {[weak self] _ in
            DispatchQueue.main.async {
                self?.tableView.reloadData()
            }
        })
        .store(in: &cancellables)
        
        viewModel?.$errorMessage.sink(receiveValue: {[weak self]  errorMessage in
            DispatchQueue.main.async {
                self?.showError(errorMessage ?? "")
            }
        })
        .store(in: &cancellables)
    }
    
    func showError(_ errorMessage: String) {
        print("there was an issue \(errorMessage)")
    }

    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return self.viewModel?.resturants.count ?? 0
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: RestaurantCell.identifier, for: indexPath) as! RestaurantCell
        
        if let resturant = viewModel?.resturants[indexPath.row] {
            cell.configureCell(resturant.name, resturant.description)
        }
        
        return cell
    }
    

}

