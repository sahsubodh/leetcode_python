//
//  PraticeTableViewTests.swift
//  PraticeTableViewTests
//
//  Created by Subodh Sah on 1/20/24.
//

import XCTest
@testable import PraticeTableView

/*
class MockNetworkService: NetworkServiceProtocol {
    
    var restaurantsToReturn: [Restaurant]?
    var errorToReturn: Error?

    func fetchRestaurants(completion: @escaping (Result<[Restaurant], Error>) -> Void) {
        if let error = errorToReturn {
            completion(.failure(error))
        } else if let restaurants = restaurantsToReturn {
            completion(.success(restaurants))
        }
    }
}
 */

class MockNetworkService: NetworkServiceProtocol {
    
    var fetchMockResult: Result<[Restaurant], Error>?

    func fetchRestaurants(completion: @escaping (Result<[Restaurant], Error>) -> Void) {
        if let result = fetchMockResult {
          completion(result)
        }
    }
}

final class PraticeTableViewTests: XCTestCase {
    
    var sut: ResturantViewModel!
    var networkService: MockNetworkService!

    override func setUp()  {
        super.setUp()

        networkService = MockNetworkService()
        sut = ResturantViewModel(networkService: networkService)
    }

    override func tearDown() {
        sut = nil
        networkService = nil
        super.tearDown()
    }

    func testLoadRestaurantsSuccess() throws {
        // Arrange
         let expectedRestaurants = [Restaurant(status: "Pending", description: "test", deliveryFee: 10, coverImgUrl: "", id: 1, name: "indian")]
         networkService.fetchMockResult = .success(expectedRestaurants)

         let expectation = XCTestExpectation(description: "Fetch restaurants")

         // Act
         sut.loadRestaurants()

         // Add a listener for the published restaurants array
         let cancellable = sut.$restaurants.sink { restaurants in
             if !restaurants.isEmpty {
                 expectation.fulfill()
             }
         }

         wait(for: [expectation], timeout: 5)

         // Assert
         XCTAssertEqual(sut.restaurants, expectedRestaurants)

         // Cancel the subscription
         cancellable.cancel()
    }
    
    func testLoadRestaurantsFailure() {
        func testLoadRestaurantsFailure() throws {
            // Arrange
            let expectedError = NSError(domain: "com.test", code: -1, userInfo: [NSLocalizedDescriptionKey: "Test Error"])
            networkService.fetchMockResult = .failure(expectedError)

            let expectation = XCTestExpectation(description: "Fetch restaurants failure")

            // Act
            sut.loadRestaurants()

            // Add a listener for the published error message
            let cancellable = sut.$errorMessage.sink { errorMessage in
                if errorMessage != nil {
                    expectation.fulfill()
                }
            }

            wait(for: [expectation], timeout: 5)

            // Assert
            XCTAssertEqual(sut.errorMessage, expectedError.localizedDescription)

            // Cancel the subscription
            cancellable.cancel()
        }
    }

}
