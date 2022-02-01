//
//  CreateViewController.swift
//  FiPay-eWallet
//
//  Created by user212276 on 2/1/22.
//

import UIKit
import Firebase

class CreateViewController: UIViewController {

    
    @IBOutlet weak var fullName: UITextField!
    @IBOutlet weak var email: UITextField!
    @IBOutlet weak var password: UITextField!
    @IBOutlet weak var cpf: UITextField!
    @IBOutlet weak var country: UITextField!
    @IBOutlet weak var state: UITextField!
    @IBOutlet weak var city: UITextField!
    @IBOutlet weak var street: UITextField!
    @IBOutlet weak var createButton: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        createButton.layer.cornerRadius = 8
        
    }
    
    @IBAction func createAccountPressed(_ sender: UIButton) {
        
        if let email = email.text, let password = password.text {
            Auth.auth().createUser(withEmail: email, password: password) { authResult, error in
                if let e = error {
                    print(e.localizedDescription)
                } else {
                    self.performSegue(withIdentifier: "RegisterToHome", sender: self)
                }
                
            }
        }
        
        
    }
    
    
}
