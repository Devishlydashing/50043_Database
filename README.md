# 50.043---Database

## API Documentation

### **Get A Review**

- **URL:**
  `/review/`

- **Method:**
  `GET`
- **URL Params**
  **Required:**
  `id=[String]`

- **Success Response:**

  - **Code:** 200 <br />
    **Content:** `{ "asin": "B000ZC8DPM", "helpful": "[0, 0]", "id": 1000, "overall": 5, "reviewText": "Stephanie Bond has become my new favorite author! She is really great at bringing a story together and keeping you hanging on to the end. I find it hard to put her books down once I start!", "reviewTime": "10 7, 2012", "reviewerID": "AR5WJIS4HEHNE", "reviewerName": "LittleByrd", "summary": "This is a really great book. Hillarious!", "unixReviewTime": 1349568000 }`

- **Error Response:**

  - **Code:** 404 <br />
    **Content:** `{"message": "There is no review with id 10003"}`

### **Add A Review**

- **URL:**
  `/review/`

- **Method:**
  `POST`

- **Data Param:**

  `{ "asin": "B000ZC8DPM", "reviewText": "Stephanie Bond has become my new favorite author! She is really great at bringing a story together and keeping you hanging on to the end. I find it hard to put her books down once I start!", "reviewerID": "AR5WJIS4HEHNE", "reviewerName": "LittleByrd", "summary": "This is a really great book. Hillarious!" }`

- **Success Response:**

  - **Code:** 200 <br />
    **Content:** `{ "id": 982626, "asin": "B000ZC8DPM", "helpful": "[0, 0]", "overall": 0, "reviewText": "Stephanie Bond has become my new favorite author! She is really great at bringing a story together and keeping you hanging on to the end. I find it hard to put her books down once I start!", "reviewTime": "2020-11-21", "reviewerID": "AR5WJIS4HEHNE", "reviewerName": "LittleByrd", "summary": "This is a really great book. Hillarious!", "unixReviewTime": 1605890900 }`

- **Error Response:**

  - **Code:** 500 <br />
    **Content:** `{"message": "An error occurred when inserting review"}`

  OR

  - **Code:** 400 <br />
    **Content:** `{"message": {"asin": "This field cannot be left blank!"}}`

### **Delete A Review**

- **URL:**
  `/review/`

- **Method:**
  `DELETE`
- **URL Params**
  **Required:**
  `id=[String]`

- **Success Response:**

  - **Code:** 200 <br />
    **Content:** `{"message": "Review of id 10003 deleted"}`

- **Error Response:**

  - **Code:** 404 <br />
    **Content:** `{"message": "There is no review with id 10003"}`

---

### **Get Reviews**

- **URL:**
  `/reviews/`

- **Method:**
  `GET`
- **URL Params**
  **Required:**
  `asin=[String]`

- **Success Response:**

  - **Code:** 200 <br />
    **Content:** `[ { "asin": "B000ZC8DPM", "helpful": "[0, 0]", "id": 988, "overall": 5, "reviewText": "Love Stephanie Bond! Comical stories, keeps you wanting more. Can't wait for another one. Romance an clumsiness with a little calamity lol!", "reviewTime": "12 28, 2012", "reviewerID": "A3AU6XLPV4QUPB", "reviewerName": "Aissa", "summary": "Naughty or nice?", "unixReviewTime": 1356652800 }, . . ., { "asin": "B000ZC8DPM", "helpful": "[0, 0]", "id": 989, "overall": 3, "reviewText": "I tried this book because I wanted something light and happy for this Christmas season. I was very surprised to find it concerned an older hotel in San Francisco, one of my most favorite cities. The heroine was a strong woman and she meets a man who is ", "reviewTime": "12 20, 2013", "reviewerID": "A3BLREOY1EY3DC", "reviewerName": "Bama Girl", "summary": "Not yourUsual Christmas Story", "unixReviewTime": 1387497600 } ]`

- **Error Response:**

  - **Code:** 404 <br />
    **Content:** `{"message": "There are no reviews with asin B000ZC8DPMa"}`

### **Delete Reviews**

- **URL:**
  `/reviews/`

- **Method:**
  `DELETE`
- **URL Params**
  **Required:**
  `asin=[String]`

- **Success Response:**

  - **Code:** 200 <br />
    **Content:** `{"message": "Review of asin B000FA64PA deleted"}`

- **Error Response:**

  - **Code:** 404 <br />
    **Content:** `{"message": "There are no reviews with asin B000FA64PA"}`

## **Get All Books**

- **URL:**
  `/allbooks`

- **Method:**
  `GET`

- **Success Response:**

  - **Code:** 200 <br />
    **Content:** `{ [{"_id": {"$oid": "5f89a3b947ad505b9ce7ee7e"}, "asin": "B000FA5SHK", "imUrl": "http://ecx.images-amazon.com/images/I/51c7mqORjsL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg", "categories": [["Books", "Science & Math", "Behavioral Sciences"], ["Books", "Self-Help", "Relationships", "Love & Romance"], ["Books", "Self-Help", "Sex"], ["Kindle Store", "Kindle eBooks", "Health, Fitness & Dieting", "Relationships", "Love & Romance"], ["Kindle Store", "Kindle eBooks", "Health, Fitness & Dieting", "Sex"]]}, . . ., {"_id": {"$oid": "5f89a3b947ad505b9ce7ee85"}, "asin": "B000FA5MQ2", "description": "PreTest&#174; is the medical student's most dynamic weapon for mastering the USMLE Step 2. *Designed to simulate the USMLE Step 2 *Reviewed by recently tested students *Mimics the real exam, question by question PreTest is the closest you can get to seeing the test before you take it. This one-of-a-kind test prep guide helps you: *Get to know material on the actual exam *Practice with 500 multiple-choice questions, many with clinical vignettes *Build confidence, skills, and knowledge *Learn key facts *Find references with every answer There are plenty of answers out there. But only PreTest&#174; delivers USMLE-type questions, in USMLE format. Open this PreTest for: *Format that simulates the exam *500 board-type questions *Referenced answers *Best prep there is for preventive medicine and public health questions on the USMLE Step 2 Great for course review and clinical rotations, too! Preventive Medicine and Public Health PreTest asks the right questions so you'll know the right answers. Open it and start learning what's on the test. &#x22;The annotated answers are a strength of this book&#8230;The types of questions in the manuscript parallel the format of those on the USMLE Step 2.&#x22; --a medical student who recently passed the USMLE Step 2", "price": 2.99, "imUrl": "http://ecx.images-amazon.com/images/I/41q97gzhKWL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg", "related": {"also_bought": ["B0054RFZGI", "B004M8SLRK", "B005OLBF3G", "B00B98WIOI", "B005H6VHMM", "B009Q0CS78", "B00EAR8UB0", "B00AN7MSPU", "B001VCD7V0"], "buy_after_viewing": ["B0054RFZGI"]}, "categories": [["Books", "Medical Books", "Medicine", "Internal Medicine", "Epidemiology"], ["Books", "Medical Books", "Medicine", "Preventive Medicine"], ["Books", "Medical Books", "Medicine", "Test Preparation & Review"], ["Kindle Store", "Kindle eBooks", "Professional & Technical", "Medical eBooks", "Administration & Policy", "Public Health"], ["Kindle Store", "Kindle eBooks", "Professional & Technical", "Medical eBooks", "Education & Training"], ["Kindle Store", "Kindle eBooks", "Professional & Technical", "Medical eBooks", "Internal Medicine", "Infectious Disease", "Epidemiology"], ["Kindle Store", "Kindle eBooks", "Professional & Technical", "Medical eBooks", "Specialties", "Preventive Medicine"]]}] }`

- **Error Response:**

  - **Code:** 404 <br />
    **Content:** ``

### **Get A Book**

- **URL:**
  `/metadata/<asin>`

- **Method:**
  `GET`
- **URL Params**
  **Required:**
  `asin=[int]`

- **Success Response:**

  - **Code:** 201 <br />
    **Content:** `{ "data": "{'_id': ObjectId('5f89a3b947ad505b9ce7ee8f'), 'asin': 'B0002IQ15S', 'categories': [['Kindle Store', 'Kindle Accessories', 'Power Adapters', 'Kindle (1st Generation) Adapters']], 'description': \"This universal DC adapter powers/charges portable electronic devices such as mobile phones, handhelds/PDAs, digital cameras and MP3 players. Utilizing interchangeable itips, iGo AutoPower powers/charges virtually all of your portable electronic devices from any standard auto power outlet eliminating the need to carry multiple power adapters when you're mobile.Main FeaturesManufacturer: Mobility Electronics, IncManufacturer Part Number: PS0221-10Manufacturer Website Address: www.mobilityelectronics.comProduct Type: Power AdapterInput Voltage: 11.5 V DC to 16 V DCOutput Power: 15WWeight: 3.6 ozStandard Warranty: 2 Year(s) Limited\", 'title': 'Mobility IGO AUTOPOWER 3000 SERIES ( PS0221-10 )', 'price': 19.99, 'salesRank': {}, 'imUrl': 'http://ecx.images-amazon.com/images/I/21QFJM28NGL.jpg', 'related': {'also_viewed': ['B00511PS3C', 'B000PI17MM', 'B0016L6OWK', 'B006BGZJJ4', 'B005DOKHLK', 'B001W1XT6I', 'B003YLMAC8', 'B00EXIGQFS', 'B000QSPO3Y', 'B001W1TZTS', 'B00115PYGS', 'B001W1XT5O', 'B002GJQ7AU', 'B00EOE6COQ', 'B0012J52OC', 'B001007OUI', 'B00F3HH2HY', 'B00CGIVV5C', 'B00GA567M4', 'B002WCCQQA', 'B006GWO5NE', 'B006GWO5WK', 'B007HCCNJU', 'B00BHJRYYS'], 'buy_after_viewing': ['B006GWO5WK', 'B001N2LHHO', 'B006GWO5NE', 'B0012J52OC']}}", "message": "Book's metadata exists" }`

- **Error Response:**

  - **Code:** 404 <br />
    **Content:** `"data": {}, "message": "Book's metadata does not exists"`

### **Add a new Book**

- **URL:**
  `/bookPost`

- **Method:**
  `POST`

- **URL Params**
  **Required:**
  `asin=[int] AND title=[String] AND price=[float] AND category=[String]`

- **Success Response:**

  - **Code:** 201 <br />
    **Content:** `{ "data": "<pymongo.results.InsertOneResult object at 0x000001F0AC92D280>", "message": "Book added" }`

- **Error Response:**

  - **Code:** 404 <br />
    **Content:** `"data": {}, "message": "Book exists. Please select another one!"`

### **Searching for a book based on title / author / category**

- **URL:**
  `/bookSearch`

- **Method:**
  `GET`

- **URL Params**
  **Required:**
  `page=[int] AND EITHER title=[String] OR title=[String] OR category=[String]`

- **Success Response:**

  - **Code:** 201 <br />
    **Content:** `{"_id": {"$oid": "5f89a3b947ad505b9ce7ee8f"}, "asin": "B0002IQ15S", "categories": [["Kindle Store", "Kindle Accessories", "Power Adapters", "Kindle (1st Generation) Adapters"]], "description": "This universal DC adapter powers/charges portable electronic devices such as mobile phones, handhelds/PDAs, digital cameras and MP3 players. Utilizing interchangeable itips, iGo AutoPower powers/charges virtually all of your portable electronic devices from any standard auto power outlet eliminating the need to carry multiple power adapters when you're mobile.Main FeaturesManufacturer: Mobility Electronics, IncManufacturer Part Number: PS0221-10Manufacturer Website Address: www.mobilityelectronics.comProduct Type: Power AdapterInput Voltage: 11.5 V DC to 16 V DCOutput Power: 15WWeight: 3.6 ozStandard Warranty: 2 Year(s) Limited", "title": "Mobility IGO AUTOPOWER 3000 SERIES ( PS0221-10 )", "price": 19.99, "salesRank": {}, "imUrl": "http://ecx.images-amazon.com/images/I/21QFJM28NGL.jpg", "related": {"also_viewed": ["B00511PS3C", "B000PI17MM", "B0016L6OWK", "B006BGZJJ4", "B005DOKHLK", "B001W1XT6I", "B003YLMAC8", "B00EXIGQFS", "B000QSPO3Y", "B001W1TZTS", "B00115PYGS", "B001W1XT5O", "B002GJQ7AU", "B00EOE6COQ", "B0012J52OC", "B001007OUI", "B00F3HH2HY", "B00CGIVV5C", "B00GA567M4", "B002WCCQQA", "B006GWO5NE", "B006GWO5WK", "B007HCCNJU", "B00BHJRYYS"], "buy_after_viewing": ["B006GWO5WK", "B001N2LHHO", "B006GWO5NE", "B0012J52OC"]}}`

- **Error Response:**

  - **Code:** 404 <br />
    **Content:** `{"message": "Book does not exists!", "data": {}}`

### **Deleting a book**

- **URL:**
  `/metadelete/<asin>`

- **Method:**
  `DELETE`

- **URL Params**
  **Required:**
  `asin=[int]`

- **Success Response:**

  - **Code:** 201 <br />
    **Content:** `"data": "{'_id': ObjectId('5f983bd4b54d69d3727654b9'), 'asin': 'B000FA5NS3434', 'description': 'TestTestsda', 'price': 100}", "message": "Deleted metadata of book"`

- **Error Response:**

  - **Code:** 404 <br />
    **Content:** `"data": {}, "message": "Book does not exist so cannot delete metadata"`
