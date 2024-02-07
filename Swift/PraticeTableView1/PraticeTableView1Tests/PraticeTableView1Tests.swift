//
//  PraticeTableView1Tests.swift
//  PraticeTableView1Tests
//
//  Created by Subodh Sah on 1/22/24.
//

import XCTest
@testable import PraticeTableView1

class MockNetworkService: NetworkServiceProtocol {
    var response : Result<[Restaurant], Error>?
    func getResturants(completion: @escaping (Result<[Restaurant], Error>) -> Void) {
        if let response = response {
            completion(response)
        }
    }
}

final class PraticeTableView1Tests: XCTestCase {
    
    var sut : RestaurantViewModel!
    var networkService: MockNetworkService!

    override func setUp()  {
        super.setUp()
        
        let networkService = MockNetworkService()
        let sut = RestaurantViewModel(networkService: networkService)

    }

    override func tearDown()  {
        networkService = nil
        sut = nil
        super.tearDown()
    }
    
    func testAPISuccess() {
        //arrange
        let expectedRestaurants = [Restaurant(status: "Pending", description: "test", deliveryFee: 10, coverImgUrl: "", id: 1, name: "indian")]
        networkService.response = .success(expectedRestaurants)
        //act
        let expectation = XCTestExpectation(description: "Fetch restaurants")
        
        sut.fetchRestaurants()
        
        let cancellable = sut.$resturants.sink { restaurants in
            if !restaurants.isEmpty {
                expectation.fulfill()
            }
        }
        
        wait(for: [expectation],timeout: 5)
        //assert
        
        XCTAssertEqual(sut.resturants, expectedRestaurants)
        cancellable.cancel()
        
    }

    func testExample() throws {
        
    }

}
