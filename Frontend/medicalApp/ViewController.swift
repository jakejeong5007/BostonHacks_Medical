//
//  ViewController.swift
//  medicalApp
//
//  Created by sam pang on 11/18/23.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        item1.layer.masksToBounds = true
        item1.layer.cornerRadius = 5
    }
    @IBOutlet weak var item1: UILabel!
    
    @IBOutlet weak var item2: UILabel!
    
    @IBOutlet weak var item3: UILabel!
    
    @IBOutlet weak var item4: UILabel!
    
    
}

