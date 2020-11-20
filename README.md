# 50.043---Database

## API Documentation

**Get A Review**
----

* **URL:**
  `/review/`

* **Method:**
  `GET` 
  
*  **URL Params**
   **Required:**
   `id=[String]`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{
    "asin": "B000ZC8DPM",
    "helpful": "[0, 0]",
    "id": 1000,
    "overall": 5,
    "reviewText": "Stephanie Bond has become my new favorite author!  She is really great at bringing a story together and keeping you hanging on to the end.  I find it hard to put her books down once I start!",
    "reviewTime": "10 7, 2012",
    "reviewerID": "AR5WJIS4HEHNE",
    "reviewerName": "LittleByrd",
    "summary": "This is a really great book.  Hillarious!",
    "unixReviewTime": 1349568000
}`
 
* **Error Response:**

  * **Code:** 404  <br />
    **Content:** `{"message": "There is no review with id 10003"}`



**Add A Review**
----
* **URL:**
  `/review/`

* **Method:**
  `POST` 

* **Data Param:**

  `{
    "asin": "B000ZC8DPM",
    "reviewText": "Stephanie Bond has become my new favorite author!  She is really great at bringing a story together and keeping you hanging on to the end.  I find it hard to put her books down once I start!",
    "reviewerID": "AR5WJIS4HEHNE",
    "reviewerName": "LittleByrd",
    "summary": "This is a really great book.  Hillarious!"
    }`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{
    "id": 982626,
    "asin": "B000ZC8DPM",
    "helpful": "[0, 0]",
    "overall": 0,
    "reviewText": "Stephanie Bond has become my new favorite author!  She is really great at bringing a story together and keeping you hanging on to the end.  I find it hard to put her books down once I start!",
    "reviewTime": "2020-11-21",
    "reviewerID": "AR5WJIS4HEHNE",
    "reviewerName": "LittleByrd",
    "summary": "This is a really great book.  Hillarious!",
    "unixReviewTime": 1605890900
}`
 
* **Error Response:**
  * **Code:** 500  <br />
    **Content:** `{"message": "An error occurred when inserting review"}`

  OR

  * **Code:** 400 <br />
    **Content:** `{"message": {"asin": "This field cannot be left blank!"}}`

**Delete A Review**
----

* **URL:**
  `/review/`

* **Method:**
  `DELETE` 
  
*  **URL Params**
   **Required:**
   `id=[String]`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{"message": "Review of id 10003 deleted"}`
 
* **Error Response:**

  * **Code:** 404  <br />
    **Content:** `{"message": "There is no review with id 10003"}`

------------------------------
**Get Reviews**
----

* **URL:**
  `/reviews/`

* **Method:**
  `GET` 
  
*  **URL Params**
   **Required:**
   `asin=[String]`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `[
    {
        "asin": "B000ZC8DPM",
        "helpful": "[0, 0]",
        "id": 988,
        "overall": 5,
        "reviewText": "Love Stephanie Bond! Comical stories, keeps you wanting more. Can't wait for another one. Romance an clumsiness with a little calamity lol!",
        "reviewTime": "12 28, 2012",
        "reviewerID": "A3AU6XLPV4QUPB",
        "reviewerName": "Aissa",
        "summary": "Naughty or nice?",
        "unixReviewTime": 1356652800
    }, . . ., {
        "asin": "B000ZC8DPM",
        "helpful": "[0, 0]",
        "id": 989,
        "overall": 3,
        "reviewText": "I tried this book because I wanted something light and happy for this Christmas season.  I was very surprised to find it concerned an older hotel in San Francisco, one of my most favorite cities.  The heroine was a strong woman and she meets a man who is ",
        "reviewTime": "12 20, 2013",
        "reviewerID": "A3BLREOY1EY3DC",
        "reviewerName": "Bama Girl",
        "summary": "Not yourUsual Christmas Story",
        "unixReviewTime": 1387497600
    } ]`
 
* **Error Response:**

  * **Code:** 404  <br />
    **Content:** `{"message": "There are no reviews with asin B000ZC8DPMa"}`

**Delete Reviews**
----

* **URL:**
  `/reviews/`

* **Method:**
  `DELETE` 
  
*  **URL Params**
   **Required:**
   `asin=[String]`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{"message": "Review of asin B000FA64PA deleted"}`
 
* **Error Response:**

  * **Code:** 404  <br />
    **Content:** `{"message": "There are no reviews with asin B000FA64PA"}`
