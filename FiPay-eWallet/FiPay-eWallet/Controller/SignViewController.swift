//
//  SignViewController.swift
//  FiPay-eWallet
//
//  Created by user212276 on 2/1/22.
//

import UIKit
import Firebase

class SignViewController: UIViewController {
    
    
    @IBOutlet weak var fieldEmail: UITextField!
    @IBOutlet weak var fieldPassword: UITextField!
    @IBOutlet weak var singOutlet: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        singOutlet.layer.cornerRadius = 8
        
    }
    
    
    @IBAction func SignInButton(_ sender: UIButton) {
        
        if let email = fieldEmail.text, let password = fieldPassword.text {
            Auth.auth().signIn(withEmail: email, password: password) { authResult, error in
                if let e = error {
                    print(e.localizedDescription)
                } else {
                    self.performSegue(withIdentifier: "goToHome", sender: self)
                }
            }
        }
        
    }
    
    
}
