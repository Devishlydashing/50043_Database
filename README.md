# 50.043---Database

## API Documentation

## **Get A Review**

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

## **Add A Review**

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

## **Delete A Review**

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

## **Get Reviews**

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

## **Delete Reviews**

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
    **Content:** `{ [{"_id": {"$oid": "5f89a3b947ad505b9ce7ee7e"}, "asin": "B000FA5SHK", "imUrl": "http://ecx.images-amazon.com/images/I/51c7mqORjsL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg", "categories": [["Books", "Science & Math", "Behavioral Sciences"], ["Books", "Self-Help", "Relationships", "Love & Romance"], ["Books", "Self-Help", "Sex"], ["Kindle Store", "Kindle eBooks", "Health, Fitness & Dieting", "Relationships", "Love & Romance"], ["Kindle Store", "Kindle eBooks", "Health, Fitness & Dieting", "Sex"]]}, {"_id": {"$oid": "5f89a3b947ad505b9ce7ee7f"}, "asin": "B000FA5UXC", "imUrl": "http://ecx.images-amazon.com/images/I/51q4iur5ukL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg", "related": {"also_bought": ["B004SPL1I8", "B00942QL3K", "B000FA5Q8Q", "B003E4CYVW", "B003P9XMEE"]}, "categories": [["Books", "Literature & Fiction"], ["Books", "Science Fiction & Fantasy", "Science Fiction", "High Tech"], ["Kindle Store", "Kindle eBooks", "Science Fiction & Fantasy", "Science Fiction", "Hard Science Fiction"]], "description": "Madoc Tamlin is a man with an unusual problem. He wakes to find himself a thousand years in the future, in a space station on the far side of the sun. Or so he is told by the mysterious, sexless human who greets him. Madoc assures himself that he's still in his own time, trapped in advanced virtual reality by one of his foes, because if he isn't, he has no idea why he was cryogenically frozen--which would mean that he was a dangerous criminal. And he doesn't remember that either! Plus, the notorious serial killer Christine Caine has been defrosted to join him, and they, along with their strange rescuer, have just been captured in an impossible space battle by an unknown enemy.The Omega Expeditionis the sixth and concluding volume of Brian Stableford's grand future history, which explores the possibilities and perils of emortality (near-immortality). This is one of the most thoughtful, complex, and ambitious series ever produced in science fiction, and its final novel, a standalone work, masterfully orchestrates the numerous characters, themes, plot lines, and ideas to a bold conclusion. But newcomers to the series really shouldn't start withThe Omega Expedition. Read the novels of this future history in the author's intended order, detailed in his informative introduction toThe Omega Expedition. Start withThe Cassandra Complex.--Cynthia Ward"}, {"_id": {"$oid": "5f89a3b947ad505b9ce7ee80"}, "asin": "B000FA66LM", "price": 0.99, "imUrl": "http://ecx.images-amazon.com/images/I/21DFY5029SL._BO2,204,203,200_PIsitb-sticker-v3-xsmall,TopRight,2,-18_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg", "related": {"also_bought": ["B000FA66XU", "B003U2RVSY", "B003U2RVJI", "B00H5A9QUI", "B008XT3QZG", "B002WPZV7S", "B002K8QXW4", "B003N7OVCA", "B004ZG6R4I", "B0091G4L9K", "B005WD7ALW", "B007T3N6SO", "B003N9AZNW", "B007T3NQ7U", "B008AMSF7A", "B007T3NMGA", "B00EK7QLSE", "B008XT3QOW", "B005N4A12U", "B007L3K1GC", "B006BHMD4C", "B002JVWRYU", "B0089I41K0", "B00BM5KSPE", "B009K4MKOG", "B00C4LWNO4", "B003O86R5M", "B00GR9TBWQ", "B007PG4NSW", "B004NSV4D2", "B00A07FMZG", "B00C8G374A", "B002G9UHVA", "B002GYVWAK", "B0081NRRAE", "B0089I3Z5W", "B004GHN6Z4", "B004DERHGO", "B004GNFV0Q", "B0028ADJWG", "B00HF235S0", "B0089MMT0K", "B005J5CVSU", "B003A846YK", "B005Z5HQNO", "B00CHXIWVM", "B00546SROQ", "B00FOTBZ9C", "B004KZOWEG", "B007L311N4", "B003R7L6GA", "B007YUYWQM", "B0058DIA9W", "B002K8PTLU", "B004PLO68M", "B008NG22FY", "B00DCN4PTO", "B0024NJVKG", "B001FB5ST6", "B00D29TQ5G", "B00DK5YWRY", "B00ERSK0OM", "B007704KZM", "B00AI2TO8E", "B007G9WTK2", "B0036Z9VFG", "B004RVS050"], "buy_after_viewing": ["B003N7OVCA", "B000FA66XU", "B002WPZV7S", "B002K8QXW4"]}, "categories": [["Books", "Literature & Fiction", "Genre Fiction", "Action & Adventure"], ["Kindle Store", "Kindle eBooks", "Literature & Fiction", "Action & Adventure"]]}, {"_id": {"$oid": "5f89a3b947ad505b9ce7ee81"}, "asin": "B000FA64QO", "price": 5.99, "imUrl": "http://ecx.images-amazon.com/images/I/51h5NLeMStL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg", "related": {"also_bought": ["B00513D3F0", "B00513HJW8", "B00513FPEC", "B000FA64PK", "B00513F9KM", "B00513HJN2", "B00513F9JS", "B00513HX6U", "B00513DHJ2", "B00513FP24", "B00513E6E2", "B00513H3WE", "B00513H3I8", "B00513F934", "B003F3PKFE", "B000FCKKOE", "B000FBFMVG", "B000FCKMDS", "B00513HWT8", "B000GCFCIM", "B00513HX4W", "B000FC1MZU", "B000FC1BN8", "B000JMKNQ0", "B000FBFNQ0", "B000FBFNQK", "B000FBFNQA", "B000WJQU26", "B0010SENMC", "B000SEGVBA", "B000SEFLNY", "B000UZQHX4", "B000SEGWWI", "B000VTUDR0", "B0018C6Y36", "B000FA64PA", "B000XPNUTU", "B001FA0I7Y", "B00A9ET67K", "B00513H3GU", "B001NLKUMI", "B002L9MYZC", "B001NLL8RO", "B00513HX9W", "B0036S4APE", "B0036S4CDE", "B003F3PM70", "B004J4WNKS", "B004J4WM7M", "B00513HJLO", "B00513FP2Y", "B00513DGB6", "B005DXOOWE", "B00513E5NO", "B00513FPOC", "B00513DGUC", "B00513HWSE", "B00513H3RE", "B00513E5SY", "B00513E3HW", "B0064C3TO2", "B00513DGES", "B00513HJKU", "B00513HWTS", "B00513DGTI", "B00E735G9G", "B005X0JI6E", "B00513HWQG", "B00A5MRE9S", "B00513F9PW", "B00513FPBU", "B00513DGC0", "B00513D3QE", "B00B0LP3WS", "B00513DGUM", "B00513E3V8", "B005O1BYBE", "B00513F9DE", "B00513F9UM", "B00513HCR0", "B00513F9J8", "B00513F952", "B00957T528", "B00513D3B4", "B00CGI3J4S", "B00513D47M", "B008ED5HE4", "B008LMD2QI", "B00513F9FW", "B00513F92K", "B00LNRWTSU", "B004NNUYF6", "B00513HX2O", "B00513HCM0", "B00513DGYS", "B00513D4HC", "B00513DGZ2", "B00513HJXC", "B00513F9OS", "B00513F9HU"], "buy_after_viewing": ["B00513D3F0", "B000FBFNQA", "B00513F9JS", "B00513E5G6"]}, "categories": [["Books", "Literature & Fiction", "Genre Fiction", "Movie Tie-Ins"], ["Books", "Science Fiction & Fantasy", "Science Fiction", "Space Opera"], ["Kindle Store", "Kindle eBooks", "Literature & Fiction", "Genre Fiction", "Movie Tie-Ins"], ["Kindle Store", "Kindle eBooks", "Science Fiction & Fantasy", "Science Fiction", "Space Opera"], ["Kindle Store", "Kindle eBooks", "Science Fiction & Fantasy", "Science Fiction", "TV, Movie, Video Game Adaptations", "Star Wars"]]}, {"_id": {"$oid": "5f89a3b947ad505b9ce7ee82"}, "asin": "B000F83TEQ", "imUrl": "http://ecx.images-amazon.com/images/I/2136NBNV5FL._BO2,204,203,200_PIsitb-sticker-v3-xsmall,TopRight,2,-18_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg", "related": {"also_bought": ["B00IS81LFO", "B000FA5T6A", "B00IS823GA", "B00IS81QVS", "B00IS80K60", "B00IS887XI", "B00H8Y5EVG", "B00IS8824M", "B000FA5L7M", "B00IS888QO", "B00IS7ZOG2", "B00IS881AC", "B00IS811W2", "B00IS80150", "B00IS819E2", "B00AQP7DLS", "B00IS885V2", "B00B1MSJ4A", "B00IS885A8", "B00IS88N1Y", "B00IS81UIM", "B00IS814T2", "B00IS80K9W", "B00AQP7IDQ", "B0044XVC8S", "B003V4BPG0", "B003V4BPSI", "B005QBMS3A", "B004SOQ1XY", "B00AQP7IVS", "B0085OTF4A", "B005QBMJUC", "B003V4BPOC", "B005QBMQSC", "B008H766TM", "B004SOQ11G", "B00AB6BMTQ", "B008H767FK", "B00DIANILC", "B00B1MSI2I", "B00BVC1SSE", "B004SOQ0A8", "B00BMVVW4E", "B00CQETPRM", "B00F0QWBNS", "B008H76674", "B005QBMQ1E", "B00B1MSINM", "B005QBMG8W", "B00B1MSIY6"]}, "categories": [["Books", "Literature & Fiction"], ["Books", "Mystery, Thriller & Suspense", "Thrillers & Suspense", "Suspense"], ["Kindle Store", "Kindle eBooks", "Mystery, Thriller & Suspense", "Suspense"]]}, {"_id": {"$oid": "5f89a3b947ad505b9ce7ee83"}, "asin": "B000FA5M6M", "description": "Powerful Strategies to Slip Between Day Traders and Long-Term Investors&#8212;and Grab Hidden Trading Profits!Located in the gray area between the lightning-fast day trader and the endlessly patient buy-and-hold investor, the modern swing trader executes intermediate positions that offer highly lucrative results with less volatility. The Master Swing Trader contains a wealth of practical insights and information for using this powerful trading method to profit from short-term price moves often missed by other market participants. After beginning with a detailed background on Pattern Cycle applications and the trend-range axis, The Master Swing Trader presents:* Dozens of specific trading strategies and setups that include precise reward, risk, and stop-loss considerations* Concrete tips, tactics, and workflows to make informed choices at each stage of short-term trade evolution* The 7 Bells &#8211; unique tools to uncover high-probability short-term trading prospectsWith more than 200 charts and dozens of proprietary setups that illustrate both classic and highly original short-term tactics, The Master Swing Trader doesn&#8217;t leave your trading profits to chance. Coldly analytical and backed by real-time trading results, this proven course for short-term traders will help you improve your bottom line, lessen your risks&#8212;and increase your confidence in building solid profits in today&#8217;s volatile markets!Biased news stories spun by insiders to manipulate options prices&#8230;Questionable stocks pushed by analysts so their trading departments can unload bloated inventories &#8230; Quick-trigger day traders chasing the latest chat room buzz &#8230;Today&#8217;s top market players understand that our &#x22;efficient&#x22; markets are actually highly inefficient, driven by insiders with hidden agendas and an irrational pack mentality that has little to do with underlying value. Fortunately, this constant imbalance generates repeated, high-probability trade setups&#8212;and Alan Farley&#8217;s The Master Swing Trader reveals how you can find and profit from these difficult-to-spot opportunities before they disappear.Farley&#8217;s innovative system is based on Pattern Cycles&#8212;shifting market stages that repeat in an orderly, predictable process through all price charts and time frames. These classic Pattern Cycles:* Describe the machine language within market opportunity* Reveal the origin of the trade setup* Explain how to capitalize on inefficiency through every bull and bear phase* Show exactly where to uncover consistent profit opportunities* Offer natural methods to shift tactics quickly as conditions change* Predict the impact of the emotional crowd on trend, range, and price developmentThe Master Swing Trader will help you apply Pattern Cycles to your advantage, over and over again. By encompassing virtually all market action, and revealing how price moves in a highly predictable manner, its powerful tools will give you the edge you need to take other people&#8217;s money before they take yours.In today&#8217;s lightning-fast markets, open information makes profit opportunities decidedly more difficult to spot and capitalize upon&#8212;with the investing herd becoming far more skilled at spotting inefficiencies and closing them up quickly. The Master Swing Trader will teach you to recognize these trade setups one step ahead of the crowd, dive in for solid profits, and close out your position before the majority has even caught on.Pattern Cycles are not easy or automatic; they require concentration, discipline, and skilled execution. But the payoff of these classic strategies is virtually unlimited. Turn to page 1 of The Master Swing Trader now, and open a new world of trading possibilities and profits&#8212;the world of the master swing trader!", "price": 10.95, "imUrl": "http://ecx.images-amazon.com/images/I/51JRnj3RutL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg", "related": {"also_bought": ["B003ZUXQC6", "B00E66QPCG", "B001FA0Z36", "B00959GZ5Q", "B007STBH58", "B00DGA8LZC", "B00J18ZWUU", "B00IHO4R1O", "B006V3CWDS", "B004PGMI14", "B00GG94F78", "B000W94CZ8", "B00HN83YXC", "B00HT59IWA", "B00JV8D35Q", "B00AXWLJU0", "B004UARUXQ", "B00H7JE8W8", "B004H1TBCG", "B0086KPSQC", "B00CEVGIA4", "B0067PZ87C", "B00B0H9S2S", "B007RSLN7M", "B00GM5XIQK", "B00GBHQXZC", "B008YOTBQS", "B0088ETCOA", "B006B7LSLG", "B003VIWRJA", "B00AZMZOSQ", "B006X50OPW", "B00IRR20V0", "B000VYOAWO", "B001UID8LY", "B007F2O020", "B008RWO86U", "B008RERRY8", "B00DAIOL0E", "B00E0VDEDK", "B0023SDQRG", "B000UKJSJO", "B004IWRC9S", "B00BWVKM4U", "B006RDCHJG", "B000FA5MG2", "B003ZDP2ZM", "B00JU9S9XM", "B00CQK4A12", "B00916ARYS", "B007ZHVBLS", "B007PRQGVS", "B00DW7PLLQ", "B005JC5WWU", "B004HD69MY", "B00EH0DKEC", "B00B9HTLYY", "B00F87ZMK8", "B006H0LGWS", "B00CX2QCVO", "B003NE61S0", "B009L5FFIC", "B004BKJB78", "B009WWQD08", "B007VLQQU4", "B00AJ3J4UK", "B0015DWM2K", "B00GWSY1OU", "B000SEKFG2", "B009S7B5ZK", "B005C3WV02", "B001C345CS", "B008NWF4JE", "B00HIRINRU", "B004S82RZQ", "B00FVGDJQ0", "B004X6SK0E", "B00DSGWI2G", "B0013Y1UJ2", "B000QTEA4C", "B0050JKCEU", "B007XGVPBM", "B00DY73M24", "B003WJR5PE", "B005UIYM2O", "B001KAM6U6", "B00C1NKPUE", "B00F2JFSIS", "B006402N5K", "B00H3JZ0OC", "B006YDFYW6", "B009UG7DCS", "B00772I498", "B00DUM1W3E", "B0047O2HSI", "B00BZ9WAVW"], "buy_after_viewing": ["B00E66QPCG", "B004IWRC9S", "B00DGA8LZC", "B007STBH58"]}, "categories": [["Books", "Business & Money", "Investing", "Introduction"], ["Books", "Literature & Fiction", "Contemporary"], ["Kindle Store", "Kindle eBooks", "Business & Money", "Investing", "Investing Basics"], ["Kindle Store", "Kindle eBooks", "Literature & Fiction", "Contemporary Fiction"]]}, {"_id": {"$oid": "5f89a3b947ad505b9ce7ee84"}, "asin": "B000FA5PV4", "price": 3.99, "imUrl": "http://ecx.images-amazon.com/images/I/21MYKMYAF9L._BO2,204,203,200_PIsitb-sticker-v3-xsmall,TopRight,2,-18_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg", "related": {"also_bought": ["B000FA65ZY", "B00B7TD69U", "B001AQBJDK", "B003TO68BO", "B002FDLNXI", "B00EHNIKDK", "B000FCKBDO", "B000FCK0W6", "B00LEVHH6O", "B000FC2O70", "B00JU3KVDO", "B000FCK0GW", "B00I5VFNK8", "B000FC1MDW", "B003YJF0DG", "B000FC2K5G", "B000FC1RSM", "B000FC1QQA", "B000FC2RMW", "B000FC2JNY", "B00II9EBHI", "B000FCK4GI", "B000FBJDZC", "B00HP4P8RY", "B002IPZK00", "B005MHI11G", "B000FC1B2E", "B00EBO2ET6", "B000FC2O6G", "B000FC2MC2", "B000FC2MB8", "B000FC1N0Y", "B000FC1GA6", "B000FC2O66", "B000FCKBDY", "B000FC2RN6", "B000FC1QC4", "B00K9T6DLM", "B000FC2LW8", "B000FC2RMC", "B000FBJAZU", "B000FC2RMM", "B000FCK2V0", "B00DXTRD96", "B000FCK4S6", "B005MHI0GW", "B000FCK0H6", "B000FC0XXM", "B000FC2ISU", "B000FC1LTM", "B000FC0XWS", "B000FC1TG2", "B000FC1AHU", "B000FC1RX2", "B000FCK1YS", "B00I9CIOWC", "B000FC1AHA", "B000FC1V3S", "B000FC1TGC", "B000FC1V4C", "B000FCKBE8", "B000FCKCCE", "B000FC2K4W", "B000FCKBDE", "B000FC0ZGW", "B00IYRXQTI", "B000FC1QQ0", "B000FC27SG", "B000FC2K56", "B002IPZJSI", "B000FC0ZGM", "B000FC1QP6", "B000FC1BHE", "B000FC2O6Q", "B00CKXU316", "B000FC2K4C", "B000FBJDS4", "B000FC27RW", "B000FC0ZHQ", "B000FC1QPQ", "B005MHHRVG", "B000FC1GAG", "B000FCK0GM", "B000FC0XXC", "B000FC1VPQ", "B000FBJF5U", "B000FBJAZA", "B00J15GC02", "B000FCK2VK", "B000FBJB0O", "B000FC2MBI", "B000FC1ME6", "B000FC2MBS", "B000FBJDVG", "B000FBJDZM", "B000FCK3Z0", "B000FC2PLA", "B000FC1AHK"], "buy_after_viewing": ["B001AQBJDK", "B003TO68BO", "B002FDLNXI", "B00I5VFNK8"]}, "categories": [["Books", "Literature & Fiction"], ["Books", "Mystery, Thriller & Suspense", "Thrillers & Suspense", "Suspense"], ["Kindle Store", "Kindle eBooks", "Literature & Fiction", "Genre Fiction", "Westerns", "Louis L'Amour"], ["Kindle Store", "Kindle eBooks", "Mystery, Thriller & Suspense", "Suspense"]]}, {"_id": {"$oid": "5f89a3b947ad505b9ce7ee85"}, "asin": "B000FA5MQ2", "description": "PreTest&#174; is the medical student's most dynamic weapon for mastering the USMLE Step 2. *Designed to simulate the USMLE Step 2 *Reviewed by recently tested students *Mimics the real exam, question by question PreTest is the closest you can get to seeing the test before you take it. This one-of-a-kind test prep guide helps you: *Get to know material on the actual exam *Practice with 500 multiple-choice questions, many with clinical vignettes *Build confidence, skills, and knowledge *Learn key facts *Find references with every answer There are plenty of answers out there. But only PreTest&#174; delivers USMLE-type questions, in USMLE format. Open this PreTest for: *Format that simulates the exam *500 board-type questions *Referenced answers *Best prep there is for preventive medicine and public health questions on the USMLE Step 2 Great for course review and clinical rotations, too! Preventive Medicine and Public Health PreTest asks the right questions so you'll know the right answers. Open it and start learning what's on the test. &#x22;The annotated answers are a strength of this book&#8230;The types of questions in the manuscript parallel the format of those on the USMLE Step 2.&#x22; --a medical student who recently passed the USMLE Step 2", "price": 2.99, "imUrl": "http://ecx.images-amazon.com/images/I/41q97gzhKWL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg", "related": {"also_bought": ["B0054RFZGI", "B004M8SLRK", "B005OLBF3G", "B00B98WIOI", "B005H6VHMM", "B009Q0CS78", "B00EAR8UB0", "B00AN7MSPU", "B001VCD7V0"], "buy_after_viewing": ["B0054RFZGI"]}, "categories": [["Books", "Medical Books", "Medicine", "Internal Medicine", "Epidemiology"], ["Books", "Medical Books", "Medicine", "Preventive Medicine"], ["Books", "Medical Books", "Medicine", "Test Preparation & Review"], ["Kindle Store", "Kindle eBooks", "Professional & Technical", "Medical eBooks", "Administration & Policy", "Public Health"], ["Kindle Store", "Kindle eBooks", "Professional & Technical", "Medical eBooks", "Education & Training"], ["Kindle Store", "Kindle eBooks", "Professional & Technical", "Medical eBooks", "Internal Medicine", "Infectious Disease", "Epidemiology"], ["Kindle Store", "Kindle eBooks", "Professional & Technical", "Medical eBooks", "Specialties", "Preventive Medicine"]]}] }`

- **Error Response:**

  - **Code:** 404 <br />
    **Content:** ``

## **Get A Book**

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

## **Add a new Book**

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

## **Searching for a book based on title / author / category**

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

## **Deleting a book**

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
