# ecopark

STEPS AFTER DOWNLOADING THE CODE
1. Under static folder create 4 empty folders
    1. app_download 
            - deploy your app on web and use gonative.io to covert your web app to mobile app. Store the .apk file AS ecopark in the app_download folder
        ![image](https://user-images.githubusercontent.com/95869837/148689608-7cdeada9-bda6-4341-9176-3fd896877eee.png)
        ![image](https://user-images.githubusercontent.com/95869837/148689546-a40c5abf-f8af-41fa-8443-3ef33a67f5fa.png)
    2. user_proof
    3. vehicle_image
    4. vehicle_rc
   ![image](https://user-images.githubusercontent.com/95869837/148689508-e133bbc1-1d47-464b-b40f-0d6870e1f15e.png)

       
2. edit the url whatsapp://send?text=https://ecoparkapp.herokuapp.com/static/app_download/ecopark.apk everywhere to your desired web hosted url
    Make sure it points to the apk file.
3. Create a free account in fast2sms.com. You will be credited with 50 rs as an entry credit. Copy the api key and paste it in app.py at YOUR FAST2SMS KEY
![image](https://user-images.githubusercontent.com/95869837/148689447-3c87d2b4-19eb-4074-b7b0-9bcc4a2974c1.png)

4. Create a razorpay account and get your razorpay credentials. Replace YOUR RAZORPAY CRED in app.py with your credentials
![image](https://user-images.githubusercontent.com/95869837/148690027-e5467636-7baa-416e-809d-2aa0c8b0e1e1.png)

5. Before running the app do the following in the terminal 
    >>
        python


    >>
        from app import db


    >>
        from app import EcoParks


    >>
        db.create_all()


    >>
        db.session.add(EcoParks(park_name="JP Nagar",park_address="Ecopark, 33rd Main Rd, MG Layout, JP Nagar Phase 6, J. P. Nagar, Bengaluru, Karnataka 560078",ultra_deluxe_vacancy = 50,semi_deluxe_vacancy=70,basic_vacancy=99,latitude="12.904054047384347",longitude="77.58047027186707"))


    >>
        db.session.add(EcoParks(park_name="Banashankari",park_address="Ecopark, No 43/2, Outer Ring Road Near, Kathreguppe, Banashankari 3rd Stage, Banashankari, Bengaluru, Karnataka 560085",ultra_deluxe_vacancy = 60,semi_deluxe_vacancy=80,basic_vacancy=90,latitude="12.923003699864813",longitude="77.55370098591682"))


    >>
        db.session.add(EcoParks(park_name="HSR Layout",park_address="Ecopark, Service Rd, Sector 4, HSR Layout, Bengaluru, Karnataka 560102",ultra_deluxe_vacancy = 55,semi_deluxe_vacancy=75,basic_vacancy=90,latitude="12.915361135682208",longitude="77.63938522761872"))


    >>
        db.session.add(EcoParks(park_name="Electronic city",park_address="Ecopark, Electronics City Phase 1, Electronic City, Bengaluru, Karnataka 560100",ultra_deluxe_vacancy = 80,semi_deluxe_vacancy=90,basic_vacancy=99,latitude="12.848371629224271",longitude="77.66358293413437"))


    >>
        db.session.commit()

6. Now make registrations and manage them from the admin panel

    ID:ecopark
    
    PASSWORD:123

You are good to go now

SAMPLE SCREENSHOTS
1. SIGNUP

![image](https://user-images.githubusercontent.com/95869837/148690710-df06fff5-629e-4719-9dda-7893f8167431.png)

2.OTP

![image](https://user-images.githubusercontent.com/95869837/148690718-2e618887-a4d4-4efe-ba12-a1036bcb1dc6.png)

3.Registration

![image](https://user-images.githubusercontent.com/95869837/148690779-b4b9fcd2-2e4d-46fd-8f98-49a5d6f57348.png)
![image](https://user-images.githubusercontent.com/95869837/148690828-46be1de9-5151-4a93-8515-0bee6b1716be.png)

4.Waiting page

![image](https://user-images.githubusercontent.com/95869837/148690846-140d9d1d-e8c9-4396-8f12-8f48d88de0ce.png)

5.Navbar

![image](https://user-images.githubusercontent.com/95869837/148690858-a218157a-1ddc-4af4-bcaf-483b7b13b79a.png)

6.Privacy policy

![image](https://user-images.githubusercontent.com/95869837/148690867-3bb2f0df-9bc9-4d2a-ab67-b92f64de0951.png)

6.Terms of services

![image](https://user-images.githubusercontent.com/95869837/148690871-0ac90091-6515-4ef7-9914-f74b8e3d930d.png)

![image](https://user-images.githubusercontent.com/95869837/148690876-74d41ea6-fb57-4ad7-9a72-3c57dba50aaa.png)

7.Account settings

![image](https://user-images.githubusercontent.com/95869837/148690889-d7185b54-34a5-4643-a0d5-e58b78edaf65.png)


8.Wallet

![image](https://user-images.githubusercontent.com/95869837/148690900-8f5a10f3-bc4b-4591-9e4a-7841f4556214.png)

9. Payment Gateway

![image](https://user-images.githubusercontent.com/95869837/148690933-7583519c-99ed-4251-b3bc-aa16898cb298.png)

![image](https://user-images.githubusercontent.com/95869837/148690956-f7f8d876-ba68-4db0-9f41-77805383fda4.png)

![image](https://user-images.githubusercontent.com/95869837/148690963-20cc1f82-827e-4b69-9485-bfe530b3aa3e.png)

![image](https://user-images.githubusercontent.com/95869837/148690976-417ac23b-315e-4f85-a27f-01a94c77bc6f.png)


10.Dashboard

![image](https://user-images.githubusercontent.com/95869837/148690988-5ba69cc5-b612-43eb-947a-ef0b8065f353.png)


11. Shortest route

![image](https://user-images.githubusercontent.com/95869837/148691018-aa987565-864b-48a1-a66f-8754623da931.png)


12.Select plan

![image](https://user-images.githubusercontent.com/95869837/148691037-e197b07d-6aca-48ed-a656-57cae077a8d7.png)


13.Select time and pay from wallet

![image](https://user-images.githubusercontent.com/95869837/148691051-74245ef6-21a2-4e44-aaf6-e01ae7c974c4.png)

![image](https://user-images.githubusercontent.com/95869837/148691059-2d0d16f2-7604-445d-9356-50cb50701e7d.png)


14.Dashboard after booking

![image](https://user-images.githubusercontent.com/95869837/148691067-8346d299-7a8b-41c9-b825-e8f6e133418e.png)

15.History

![image](https://user-images.githubusercontent.com/95869837/148691077-051c4723-c88a-4352-80d8-3a48a7a06532.png)







Thank you
