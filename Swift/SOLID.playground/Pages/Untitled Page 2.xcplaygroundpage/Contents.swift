//: [Previous](@previous)

import Foundation

var greeting = "Hello, playground"

/*
  1:N

 1) weekly 2) weekdays 3) based on time
 
 once a week, daily, once a month
 
 events times are consistent - recuuring
 
 events - events id , events name, event timeStamp
 
 users - users id , [events] 
 
 skip meeting also possible if holiday or OOO
 
 
 function which decides the event dates
 
 OR array of event dates based on end date
 
 */


//enum walmartHoliday: CaseIterable {
//    case christmas(let date)
////    case christmas(let date)
////    case christmas(let date)
////    case christmas(let date)
//}

enum EventFrequency: Codable {
    case daily
    case weekly
    case montly
}

//enum eventStatus yes no



struct Event: Codable {
    var eventId: String
    var eventName: String
    
    var startDate: Date
    var endDate: Date
    
    var startTime: Date
    var endTime: Date
//    var excludedDateRange :[(Date, Date)]
    
    
    
    var eventFreq: EventFrequency = .daily
}

protocol FetchingEvent {
    func getEventsBetween(_ startDate: Date, _ endDate: Date) -> [Event]
}


class EventHandling : FetchingEvent {
    
    let allEvents: [Event]
    
    init(allEvents: [Event]) {
        self.allEvents = allEvents
    }
    
    func getEventsBetween(_ startDate: Date, _ endDate: Date) -> [Event] {
        
        
        
        let filteredEvents = allEvents.filter {
            $0.startDate >= startDate && $0.endDate <= endDate
        }
        

        
        return filteredEvents
    }
}


// 1) reuseablity 2) pop 3) testing
