//
//  LoginViewModel.swift
//  ChaseLoginTest
//
//  Created by Subodh Sah on 1/11/24.
//

import Foundation
import Combine

public enum passwordState {
    case isEmpty
    case nonSufficient
    case happy
}


protocol EmailValidationProtocol : AnyObject {
    func emailValidate(email: String) -> Bool
    func passwordValidate(password: String) -> passwordState
}

final class LoginViewModel {
    @Published var email = ""
    @Published var password = ""
    
//    @Published var emailErrorMessage: String?
//    @Published var passwordErrorMessage: String?
    
//    private var cancellables = Set<AnyCancellable>()
    
    func validateEmail() -> String? {
        print("email status \(email.isEmpty)")
        return email.isEmpty ? "Email cannot be empty" : nil
    }

    func validatePassword() -> String? {
        return password.isEmpty ? "Password cannot be empty" :
               password.count < 4 ? "Password must be at least 4 characters" : nil
    }
    
//    init() {
//        
//        $email.map { email in
//            return email.isEmpty ? "Email cannot be empty" : nil
//        }.assign(to: &$emailErrorMessage)
//        
//        $password.map {password in
//            return password.isEmpty ? "Password cannot be empty" :
//            password.count < 4 ? "Password must be at least 4 characters" : nil
//        }.assign(to: &$passwordErrorMessage)
//    }
}

/*
 guard let userName = self.userNameTxt.text, !userName.isEmpty,
 let pwd = self.passwordTxt.text, !pwd.isEmpty else {
     // error handling code
     
     self.userNameHintLbl.isHidden = false
     self.userNameHintLbl.text = self.userNameTxt.text?.count ?? 0 > 0 ? "" : "Username is required"
     
     self.passwordHintLbl.isHidden = false
     self.passwordHintLbl.text = self.passwordTxt.text?.count ?? 0 > 0 ? "" : "Password is required"
     
     
     return
 }
 
 
 // handle case when password length less than 4
 if pwd.count < 4 {
     self.userNameHintLbl.isHidden = false
     self.passwordHintLbl.text = "Password must have minimum 4 characters"
 }
 
 */

/*
class LoginViewModel : NSObject, EmailValidationProtocol {
    
    func emailValidate(email: String) -> Bool {
        self.email = email
        
        return !email.isEmpty
    }
    
    func passwordValidate(password: String) -> passwordState {
        self.password = password
        
        if self.password.isEmpty {
            return .isEmpty
        } else if self.password.count < 4 {
            return .nonSufficient
        } else {
            return .happy
        }
    }
    
    var email: String = ""
    var password : String = ""
    
    weak var delegate : EmailValidationProtocol?
    
    override init() {
        super.init()
//        self.email = ""
//        self.password = ""
        self.delegate = self
    }
    
    public init(email: String, password: String) {
        self.email = email
        self.password = password
    }
}
*/
