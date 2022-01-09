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

       
2. edit the italic url whatsapp://send?text=_https://ecoparkapp.herokuapp.com/_static/app_download/ecopark.apk everywhere to your desired web hosted url
    Make sure it points to the apk file.
3. Create a free account in fast2sms.com. You will be credited with 50 rs as an entry credit. Copy the api key and paste it in app.py at YOUR FAST2SMS KEY
![image](https://user-images.githubusercontent.com/95869837/148689447-3c87d2b4-19eb-4074-b7b0-9bcc4a2974c1.png)

4. Create a razorpay account and get your razorpay credentials. Replace YOUR RAZORPAY CRED in app.py with your credentials
![image](https://user-images.githubusercontent.com/95869837/148690027-e5467636-7baa-416e-809d-2aa0c8b0e1e1.png)

5. Before running the app do the following in the terminal 
    >>python


    >>from app import db


    >>from app import EcoParks


    >>db.create_all()


    >>db.session.add(EcoParks(park_name="JP Nagar",park_address="Ecopark, 33rd Main Rd, MG Layout, JP Nagar Phase 6, J. P. Nagar, Bengaluru, Karnataka 560078",ultra_deluxe_vacancy = 50,semi_deluxe_vacancy=70,basic_vacancy=99,latitude="12.904054047384347",longitude="77.58047027186707"))


    >>db.session.add(EcoParks(park_name="Banashankari",park_address="Ecopark, No 43/2, Outer Ring Road Near, Kathreguppe, Banashankari 3rd Stage, Banashankari, Bengaluru, Karnataka 560085",ultra_deluxe_vacancy = 60,semi_deluxe_vacancy=80,basic_vacancy=90,latitude="12.923003699864813",longitude="77.55370098591682"))


    >>db.session.add(EcoParks(park_name="HSR Layout",park_address="Ecopark, Service Rd, Sector 4, HSR Layout, Bengaluru, Karnataka 560102",ultra_deluxe_vacancy = 55,semi_deluxe_vacancy=75,basic_vacancy=90,latitude="12.915361135682208",longitude="77.63938522761872"))


    >>db.session.add(EcoParks(park_name="Electronic city",park_address="Ecopark, Electronics City Phase 1, Electronic City, Bengaluru, Karnataka 560100",ultra_deluxe_vacancy = 80,semi_deluxe_vacancy=90,basic_vacancy=99,latitude="12.848371629224271",longitude="77.66358293413437"))


    >>db.session.commit()

6. Now make registrations and manage them from the admin panel
    ID:ecopark
    
    PASSWORD:Afbcx2mv

You are good to go now

Thank you
