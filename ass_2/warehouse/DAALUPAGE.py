def PAGES(n):
    sss=[];ttt=[]
    if int(n)==0:
       sss='''課程(0920):請先到 TronClass 點名'''
    if int(n)==1:
       sss='''
抽象資料型態(或 ADT）是一程式, 它是定義一組指定的數據資料及一組定義明確的操作, 並可以對這些數值做運算

An abstract data type (or ADT) is a programmer-defined data type that
specifies a set of data values and a collection of well-defined operations
that can be performed on those values
'''
    if int(n)==2:
       sss='''一組定義明確的操作可分為四類：
(1) 構造函數：創建和初始化 ADT 的新實例。
(2) 訪問器：返回包含在實例中的數據而不修改它。
(3) 強制轉換：修改一個ADT實例的內容。
(4) 迭代器：按順序處理各個數據組件

The set of operations can be grouped into four categories:
(1) Constructors: Create and initialize new instances of the ADT.
(2) Accessors: Return data contained in an instance without modifying it.
(3) Mutators: Modify the contents of an ADT instance.
(4) Iterators: Process individual data components sequentially.'''
    if int(n)==3:
       sss='''
Figure 1.2: 將 ADT 定義與其實現分開。
'''
       ttt='Figure1d2.png' 
    if int(n)==4:
       sss='''
使用抽象資料型態(或 ADT) 和專注於如何取代有幾個優點。
(1) 可專注於解決手頭的問題，而不是陷入執行細節。
(2) 可通過防止直接訪問實現來減少由於意外誤用存儲結構和數據類型而可能發生的邏輯錯誤。
(3) 可改變抽像數據類型的實現，而不必修改使用 ADT 的程序代碼。
(4) 更容易管理更大的程序並將其劃分為更小的模塊，允許團隊的不同成員在單獨的模塊上工作。

There are several advantages of working with abstract data types and focusing on the what instead of the how.
(1) We can focus on solving the problem at hand instead of getting bogged down in the implementation details.
(2) We can reduce logical errors that can occur from accidental misuse of storage structures and data types by preventing direct access to the implementation.
(3) The implementation of the abstract data type can be changed without having to modify the program code that uses the ADT.
(4) It’s easier to manage and divide larger programs into smaller modules, al- lowing different members of a team to work on the separate modules.
'''
    if int(n)==5:
       sss='''
一個簡單的 ADT 是由一個或多個單獨命名的數據字段組成，例如用於表示日期或有理數的數據字段。
複雜的 ADT 由數據值的集合組成，例如 Python 列表或字典

有許多常見的數據結構，包括陣列、鏈結、堆疊、序列和樹，僅舉幾例。所有數據結構都存儲一個值的集合，但它們在組織各個數據項的方式以及可以應用哪些操作來管理集合方面有所不同

A simple ADT is composed of a single or several individually named data fields such as those used to represent a date or rational number. The complex ADTs are composed of a collection of data values such as the Python list or dictionary.
There are many common data structures, including arrays, linked lists, stacks, queues, and trees, to name a few. All data structures store a collection of values, but differ in how they organize the individual data items and by what operations can be applied to manage the collection.'''

    if int(n)==6:
       sss='''
為了幫助讀者並避免混淆，我們定義了一些我們將在整個文本中使用的常用術語。
(1) 集合：集合是一組價值觀，各個價值觀之間沒有隱含的組織或關係。有時我們可能會將元素限制為特定的數據類型，例如整數或浮點值的集合。
(2) 容器：容器是存儲和組織集合的任何數據結構或抽像數據類型。集合的各個值稱為容器的元素，沒有元素的容器稱為空容器
(3）序列：序列是一個容器，其中元素從前到後以線性順序排列，每個按位置可訪問的元素。
(4)有序序列：有序序列是其中元素的位置基於每個元素與其後繼之間的規定關係的序列。
在計算機科學中，術語列表通常用於指代任何具有線性排序的集合
為避免混淆，我們將使用術語列表來指代 Python 提供的數據類型，並在指代前面定義的更通用的列表結構時使用術語通用列表或列表結構。

To aide the reader and to avoid confusion, we define some of the common terms we will be using throughout the text.
(1) collection: A collection is a group of values with no implied organization or relationship between the individual values. Sometimes we may restrict the elements to a specific data type such as a collection of integers or floating-point values.
(2) container: A container is any data structure or abstract data type that stores and orga- nizes a collection. The individual values of the collection are known as elements of the container and a container with no elements is said to be empty.
(3) sequence: A sequence is a container in which the elements are arranged in linear order from front to back, with each element accessible by position.
(4) sorted sequence: A sorted sequence is one in which the position of the elements is based on a prescribed relationship between each element and its successor. In computer science, the term list is commonly used to refer to any collection with a linear ordering.
To avoid confusion, we will use the term list to refer to the data type provided by Python and use the terms general list or list structure when referring to the more general list structure as defined earlier.'''

    if int(n)==7:
       sss='''
1.2 日期的抽象資料型態: 一個簡單抽像數據類型的定義，用於表示公曆中的日期。

格里高利曆是教皇格里高利十三世於 1582 年引入的，以取代儒略歷。新曆法糾正了對陰曆年的錯誤計算，並引入了閏年。
公曆的正式第一個日期是 1582 年 10 月 15 日星期五。

儒略歷是公曆的前身，由羅馬共和國獨裁者朱利安·凱撒在埃及托勒密王朝時期由希臘數學家、天文學家索西切尼計算，於公元前45年1月1日開始實施，取代舊羅馬歷。一年有12個月，大小月交替，四年有閏，平年有365天。閏年2月底增加一個閏日，年平均長度為365.25天。

https://people.biology.ucsd.edu/patrick/julian_cal.html

1.2 The Date Abstract Data Type
We provide the definition of a simple abstract data type for representing a date in the proleptic Gregorian calendar.
The Gregorian calendar was introduced in the year 1582 by Pope Gregory XIII to replace the Julian calendar. The new calendar corrected for the miscalculation of the lunar year and introduced the leap year. The official first date of the Gregorian calendar is Friday, October 15, 1582.

The Julian calendar, the predecessor of the Gregorian calendar, was calculated by the Greek mathematician and astronomer Sosichenni of Alexandria in the Ptolemaic dynasty of Egypt by Julian Caesar, the dictator of the Roman Republic, in January 45 BC It will be implemented on the 1st, replacing the old Roman calendar. There are 12 months in a year, with alternating large and small months, a leap in four years, and 365 days in a normal year. A leap day is added at the end of February in a leap year, and the annual average length is 365.25 days.'''

    if int(n)==8:
       sss='''Listing1.1'''
       ttt='Listing1d1.png' 
    if int(n)==9:
       sss='''
附註：應正確註釋 Class 定義和方法，以幫助使用者了解 Class 和/或 方法的作用。
然而，為了節省篇幅，本書中介紹的 Class 和方法通常不會包含這些註釋，因為周圍的文本提供了完整的解釋

NOTE: Class definitions and methods should be properly commented to aide the user in knowing what the class and/or methods do. To conserve space, however, classes and methods presented in this book do not routinely include these comments since the surrounding text provides a full explanation.'''
    return sss,ttt
    
