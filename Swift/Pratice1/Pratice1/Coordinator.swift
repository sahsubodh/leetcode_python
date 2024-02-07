//
//  Coordinator.swift
//  Pratice1
//
//  Created by Subodh Sah on 1/20/24.
//

import Foundation
import UIKit

enum Event {
    case buttonTapped
}

protocol Coordinator {
//    var childCoordinators: [Coordinator] { get set }
    var navigationController: UINavigationController? { get set }
    
    func eventOccured(with type: Event)
    func start()
}

protocol Coordinating {
    var coordinator: Coordinator? { get set }
}
