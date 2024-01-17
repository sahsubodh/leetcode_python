//
//  ViewController.swift
//  ChaseLoginTest
//
//  Created by Subodh Sah on 1/11/24.
//

import UIKit
import Combine

//autolayout handling
//error handling code
//arch

class ViewController: UIViewController {

    
    @IBOutlet weak var userNameTxt: UITextField!
    @IBOutlet weak var userNameHintLbl: UILabel!
    
    @IBOutlet weak var passwordTxt: UITextField!
    @IBOutlet weak var passwordHintLbl: UILabel!
    
    private var cancellables = Set<AnyCancellable>()
    
    var vm = LoginViewModel()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        self.passwordHintLbl.isHidden = true
        self.userNameHintLbl.isHidden = true
        
        setupBindings()
        
    }
    
    private func setupBindings() {
            
        userNameTxt.textPublisher
            .assign(to: \.email, on: vm)
            .store(in: &cancellables)
        
        passwordTxt.textPublisher
            .assign(to: \.password, on: vm)
            .store(in: &cancellables)
        
//        vm.$emailErrorMessage
//            .receive(on: RunLoop.main)
//            .sink{ [weak self] errorMessage in
//                self?.userNameHintLbl.text = errorMessage
//                self?.userNameHintLbl.isHidden = errorMessage == nil
//            }.store(in: &cancellables)
//        
//        vm.$passwordErrorMessage
//            .receive(on: RunLoop.main)
//            .sink {[weak self] errorMessage in
//                self?.passwordHintLbl.text = errorMessage
//                self?.passwordHintLbl.isHidden = errorMessage == nil
//                
//            }.store(in: &cancellables)
//        
        
    }


    @IBAction func loginButtonAction(_ sender: Any) {
        
        let emailError = vm.validateEmail()
        userNameHintLbl.text = emailError
        userNameHintLbl.isHidden = emailError == nil

        let passwordError = vm.validatePassword()
        passwordHintLbl.text = passwordError
        passwordHintLbl.isHidden = passwordError == nil
        
        //username is not empty
        // password not empty and Password must have minimum 4 characters
        
//        let userName = self.userNameTxt.text ?? ""
//        let pwd = self.passwordTxt.text ?? ""
//        
////        vm = LoginViewModel(email: userName, password: pwd)
//        
//        let emailStatus  = vm.emailValidate(email: userName)
//        
//        let pwdStatus: passwordState = vm.passwordValidate(password: pwd)
//        
//        if !emailStatus {
//            self.userNameHintLbl.isHidden = false
//            self.userNameHintLbl.text =  "Username is required"
//        } else {
//            self.userNameHintLbl.isHidden = true
//        }
//        
//        switch pwdStatus {
//        case .isEmpty:
//            self.passwordHintLbl.isHidden = false
//            self.passwordHintLbl.text =  "Password is required"
//        case .nonSufficient:
//            self.passwordHintLbl.isHidden = false
//            self.passwordHintLbl.text =  "Password must have minimum 4 characters"
//        case .happy:
//            self.passwordHintLbl.isHidden = true
//        }
       
        
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
        
        self.userNameHintLbl.isHidden = true
        self.passwordHintLbl.isHidden = true
         
         */
      
        
        // happy case
        
    }
}

extension UITextField {
    var textPublisher: AnyPublisher<String,Never> {
        NotificationCenter.default.publisher(for: UITextField.textDidChangeNotification, object: self)
            .compactMap {
                $0.object as? UITextField
            }.map {
                $0.text ?? ""
            }.eraseToAnyPublisher()
    }
}

