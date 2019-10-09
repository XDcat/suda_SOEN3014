## 如何运行示例代码
```angular2
cd 02 ORM
python ./Book.py
```

## 说明
1. data 文件夹，存放着数据存储文件以及存有一些样本数据 excel 文件
2. Book.py 文件
    1. Book 类，对数据进行操作，具体如下
        * 增：初始化对象后，调用 `save()`
        * 删：使用 `delete(id)`
        * 改：修改对象后，使用 `update`
        * 查：使用 `query(id)`
    2. main 函数，使用 Book 类的一些例子
        ```angular2
       cd 02 ORM
       python ./Book.py
        ```
     3. 结果展示
         ```
        D:\CS\anaconda\envs\py3\python.exe "D:/Box/Pycharm_Project/工业实践课程/02 ORM/Book.py"
        ====== 1. 从 excel 中随机找到5本书的数据，将他们保存到文件中 =======
        保存：179,《Python计算机视觉编程》,7.3,10, [瑞典] Jan Erik Solem / 朱文涛 / 袁勇 ,  人民邮电出版社 / 2014-6-10 / 69.00
        保存：202,《图解机器学习》,0,0, 杉山将 / 许永伟 ,  人民邮电出版社 / 2015-4 / 49
        保存：294,《多元统计分析导论》,0,0, (美)T.W.Anderson / 张润楚 程轶 ,  人民邮电出版社 / 2010 年12月 / 89.00元
        保存：276,《Deep Learning》,0,0, , Ohlsson Stellan / 2011-1 / $ 135.60
        保存：256,《Introduction to Pattern Recognition》,0,0, Sergios Theodoridis / Aggelos Pikrakis / Konstantinos Koutroumbas / Dionisis Cavouras ,  Academic Press / 2010-3-31 / USD 41.95
        
        ==>文件中的结果（因为原文件有数据，所以条数可能不一致）
             1349,《这是一个被改过的 book》,8.9,10000000000000000000000000000000000000, Jimmy Lin / Chris Dyer ,  Morgan and Claypool Publishers / 2010-4-30 / USD 40.00
             2,《Graphical Models Exponential Families and Variational Inference》,9.7,20, Martin J Wainwright / Michael I Jordan ,  Now Publishers Inc / December 16 2008 / USD 125.00
             111,《数据之魅》,7.9,51, （美）Philipp K. Janert / 黄权 ,  清华大学出版社 / 2012-7 / 89.00元
             214,《信用风险评分卡研究》,0,0, 马杜姆.雷法特 / 王松奇 / 林智乾 ,  社会科学文献出版社 / 2013-7 / 58.00
             153,《Recommender Systems》,7.6,17, Dietmar Jannach / Markus Zanker / Alexander Felfernig / Gerhard Friedrich ,  Cambridge University Press / 2010-9-30 / USD 65.00
             159,《这是一个被改过的 book》,7.5,10000000000000000000000000000000000000, Haralambos Marmanis / Dmitry Babenko / 阿稳 / 陈钢 ,  电子工业出版社 / 2011-11 / 65.00元
             60,《利用Python进行数据分析》,8.6,70, Wes McKinney / 唐学韬 ,  机械工业出版社 / 2013-11-18 / 89.00
             93,《Doing Data Science》,8.1,21, Rachel Schutt / Cathy O'Neil ,  O'Reilly Media / 2013-10-30 / USD 39.99
             335,《Understanding Computational Bayesian Statistics》,0,0, , Bolstad William M. / 2009-12 / 918.00元
             355,《Data Analytics》,0,0, Runkler Thomas ,  Springer Fachmedien Wiesbaden / 2012-9 / $ 45.14
             262,《这是一个被改过的 book》,0,10000000000000000000000000000000000000, , 陆旭 / 2008-12 / 20.00元
             182,《大嘴巴漫谈数据挖掘（全彩）》,7.3,28, 易向军 ,  电子工业出版社 / 2014-4 / 69.00元
             102,《神经网络原理》,8,46, Simon Haykin / 叶世伟 / 史忠植 ,  机械工业出版社 / 2004-1 / 69.00元
             319,《Nearest-Neighbor Methods in Learning and Vision》,0,0, Shakhnarovich Gregory (EDT)/ Darrell Trevor (EDT)/ Indyk Piotr (EDT) ,  Mit Pr / 2006-3 / $ 50.85
             49,《这是一个被改过的 book》,8.9,10000000000000000000000000000000000000, Jimmy Lin / Chris Dyer ,  Morgan and Claypool Publishers / 2010-4-30 / USD 40.00
             243,《这是一个被改过的 book》,0,10000000000000000000000000000000000000, Efron Bradley ,  Cambridge University Press / 2010-9 / 646.00元
             345,《模式识别中的核方法及其应用》,0,0, , 2010-2 / 28.00元
             253,《Probabilistic Reasoning in Intelligent Systems》,0,0, Judea Pearl ,  Morgan Kaufmann / 1988-09-15 / USD 106.00
             195,《走进搜索引擎》,6.9,95, , 梁斌 / 2007-1 / 49.80元
             199,《New Internet》,6.6,27, 谭磊 ,  电子工业出版社 / 2013-3 / 69.00元
             238,《这是一个被改过的 book》,0,10000000000000000000000000000000000000, Larry Wasserman ,  Springer / 2010-12-2 / USD 99.00
             96,《模式分析的核方法》,8.1,25, 肖-泰勒 / 克瑞斯天尼 ,  机械工业出版社 / 2006-1 / 48.0
             68,《机器学习(英文版)》,8.5,20, Tom M.Mitchell / 曾华军 ,  机械工业出版社 / 2003-03 / 58.0
             116,《Statistical Models》,7.9,10, David A. Freedman ,  Cambridge University Press / 2009-04-27 / USD 40.00
             371,《Handbook of Latent Semantic Analysis》,0,0, Thomas K. Landauer / Danielle S. McNamara / Simon Dennis / Walter Kintsch ,  Lawrence Erlbaum / 2007-02-15 / USD 99.00
             66,《Learning OpenCV》,8.5,165, Adrian Kaehler / Dr. Gary Rost Bradski ,  oreilly / 2008 / USD 49.99
             121,《大数据》,7.8,311, Anand Rajaraman / Jeffrey David Ullman / 王斌 ,  人民邮电出版社 / 2012-9 / 59.00元
             241,《Machine Learning》,0,0, Peter Flach ,  Cambridge University Press / 2012-11-12 / USD 60.00
             342,《Estimation of Dependences Based on Empirical Data》,0,0, Vladimir Vapnik / Kotz S. ,  Springer / 2006-03-28 / USD 69.95
             39,《这是一个被改过的 book》,9,10000000000000000000000000000000000000, Christopher D. Manning / Prabhakar Raghavan / Hinrich Schütze ,  Cambridge University Press / 2008 / $60.00
             78,《Machine Learning in Action》,8.3,110, Peter Harrington ,  Manning Publications / 2012-4-16 / GBP 29.99
             124,《数据挖掘实用机器学习技术》,7.8,142, Ian H.Witten / Eibe Frank / 董琳 / 邱泉 / 于晓峰 ,  机械工业出版社 / 2006-3 / 48.00元
             147,《神经网络》,7.7,24, [印度]Satish Kumar ,  清华大学出版社 / 2006-8 / 73.00元
             179,《Python计算机视觉编程》,7.3,10, [瑞典] Jan Erik Solem / 朱文涛 / 袁勇 ,  人民邮电出版社 / 2014-6-10 / 69.00
             202,《图解机器学习》,0,0, 杉山将 / 许永伟 ,  人民邮电出版社 / 2015-4 / 49
             294,《多元统计分析导论》,0,0, (美)T.W.Anderson / 张润楚 程轶 ,  人民邮电出版社 / 2010 年12月 / 89.00元
             276,《Deep Learning》,0,0, , Ohlsson Stellan / 2011-1 / $ 135.60
             256,《Introduction to Pattern Recognition》,0,0, Sergios Theodoridis / Aggelos Pikrakis / Konstantinos Koutroumbas / Dionisis Cavouras ,  Academic Press / 2010-3-31 / USD 41.95
        
        
        
        ====== 2. 删除其中前 2 本 =======
        删除：book_id = 179,《Python计算机视觉编程》,7.3,10, [瑞典] Jan Erik Solem / 朱文涛 / 袁勇 ,  人民邮电出版社 / 2014-6-10 / 69.00
        删除：book_id = 202,《图解机器学习》,0,0, 杉山将 / 许永伟 ,  人民邮电出版社 / 2015-4 / 49
        
        ==>文件中的结果（因为原文件有数据，所以条数可能不一致）
             1349,《这是一个被改过的 book》,8.9,10000000000000000000000000000000000000, Jimmy Lin / Chris Dyer ,  Morgan and Claypool Publishers / 2010-4-30 / USD 40.00
             2,《Graphical Models Exponential Families and Variational Inference》,9.7,20, Martin J Wainwright / Michael I Jordan ,  Now Publishers Inc / December 16 2008 / USD 125.00
             111,《数据之魅》,7.9,51, （美）Philipp K. Janert / 黄权 ,  清华大学出版社 / 2012-7 / 89.00元
             214,《信用风险评分卡研究》,0,0, 马杜姆.雷法特 / 王松奇 / 林智乾 ,  社会科学文献出版社 / 2013-7 / 58.00
             153,《Recommender Systems》,7.6,17, Dietmar Jannach / Markus Zanker / Alexander Felfernig / Gerhard Friedrich ,  Cambridge University Press / 2010-9-30 / USD 65.00
             159,《这是一个被改过的 book》,7.5,10000000000000000000000000000000000000, Haralambos Marmanis / Dmitry Babenko / 阿稳 / 陈钢 ,  电子工业出版社 / 2011-11 / 65.00元
             60,《利用Python进行数据分析》,8.6,70, Wes McKinney / 唐学韬 ,  机械工业出版社 / 2013-11-18 / 89.00
             93,《Doing Data Science》,8.1,21, Rachel Schutt / Cathy O'Neil ,  O'Reilly Media / 2013-10-30 / USD 39.99
             335,《Understanding Computational Bayesian Statistics》,0,0, , Bolstad William M. / 2009-12 / 918.00元
             355,《Data Analytics》,0,0, Runkler Thomas ,  Springer Fachmedien Wiesbaden / 2012-9 / $ 45.14
             262,《这是一个被改过的 book》,0,10000000000000000000000000000000000000, , 陆旭 / 2008-12 / 20.00元
             182,《大嘴巴漫谈数据挖掘（全彩）》,7.3,28, 易向军 ,  电子工业出版社 / 2014-4 / 69.00元
             102,《神经网络原理》,8,46, Simon Haykin / 叶世伟 / 史忠植 ,  机械工业出版社 / 2004-1 / 69.00元
             319,《Nearest-Neighbor Methods in Learning and Vision》,0,0, Shakhnarovich Gregory (EDT)/ Darrell Trevor (EDT)/ Indyk Piotr (EDT) ,  Mit Pr / 2006-3 / $ 50.85
             49,《这是一个被改过的 book》,8.9,10000000000000000000000000000000000000, Jimmy Lin / Chris Dyer ,  Morgan and Claypool Publishers / 2010-4-30 / USD 40.00
             243,《这是一个被改过的 book》,0,10000000000000000000000000000000000000, Efron Bradley ,  Cambridge University Press / 2010-9 / 646.00元
             345,《模式识别中的核方法及其应用》,0,0, , 2010-2 / 28.00元
             253,《Probabilistic Reasoning in Intelligent Systems》,0,0, Judea Pearl ,  Morgan Kaufmann / 1988-09-15 / USD 106.00
             195,《走进搜索引擎》,6.9,95, , 梁斌 / 2007-1 / 49.80元
             199,《New Internet》,6.6,27, 谭磊 ,  电子工业出版社 / 2013-3 / 69.00元
             238,《这是一个被改过的 book》,0,10000000000000000000000000000000000000, Larry Wasserman ,  Springer / 2010-12-2 / USD 99.00
             96,《模式分析的核方法》,8.1,25, 肖-泰勒 / 克瑞斯天尼 ,  机械工业出版社 / 2006-1 / 48.0
             68,《机器学习(英文版)》,8.5,20, Tom M.Mitchell / 曾华军 ,  机械工业出版社 / 2003-03 / 58.0
             116,《Statistical Models》,7.9,10, David A. Freedman ,  Cambridge University Press / 2009-04-27 / USD 40.00
             371,《Handbook of Latent Semantic Analysis》,0,0, Thomas K. Landauer / Danielle S. McNamara / Simon Dennis / Walter Kintsch ,  Lawrence Erlbaum / 2007-02-15 / USD 99.00
             66,《Learning OpenCV》,8.5,165, Adrian Kaehler / Dr. Gary Rost Bradski ,  oreilly / 2008 / USD 49.99
             121,《大数据》,7.8,311, Anand Rajaraman / Jeffrey David Ullman / 王斌 ,  人民邮电出版社 / 2012-9 / 59.00元
             241,《Machine Learning》,0,0, Peter Flach ,  Cambridge University Press / 2012-11-12 / USD 60.00
             342,《Estimation of Dependences Based on Empirical Data》,0,0, Vladimir Vapnik / Kotz S. ,  Springer / 2006-03-28 / USD 69.95
             39,《这是一个被改过的 book》,9,10000000000000000000000000000000000000, Christopher D. Manning / Prabhakar Raghavan / Hinrich Schütze ,  Cambridge University Press / 2008 / $60.00
             78,《Machine Learning in Action》,8.3,110, Peter Harrington ,  Manning Publications / 2012-4-16 / GBP 29.99
             124,《数据挖掘实用机器学习技术》,7.8,142, Ian H.Witten / Eibe Frank / 董琳 / 邱泉 / 于晓峰 ,  机械工业出版社 / 2006-3 / 48.00元
             147,《神经网络》,7.7,24, [印度]Satish Kumar ,  清华大学出版社 / 2006-8 / 73.00元
             294,《多元统计分析导论》,0,0, (美)T.W.Anderson / 张润楚 程轶 ,  人民邮电出版社 / 2010 年12月 / 89.00元
             276,《Deep Learning》,0,0, , Ohlsson Stellan / 2011-1 / $ 135.60
             256,《Introduction to Pattern Recognition》,0,0, Sergios Theodoridis / Aggelos Pikrakis / Konstantinos Koutroumbas / Dionisis Cavouras ,  Academic Press / 2010-3-31 / USD 41.95
        
        
        
        ====== 3. 重复插入刚才的 5 本 =======
        保存：179,《Python计算机视觉编程》,7.3,10, [瑞典] Jan Erik Solem / 朱文涛 / 袁勇 ,  人民邮电出版社 / 2014-6-10 / 69.00
        保存：202,《图解机器学习》,0,0, 杉山将 / 许永伟 ,  人民邮电出版社 / 2015-4 / 49
        =>错误：文件中已经存在主键 294 ，你可能需要更新操作
        =>错误：文件中已经存在主键 276 ，你可能需要更新操作
        =>错误：文件中已经存在主键 256 ，你可能需要更新操作
        
        ==>文件中的结果（因为原文件有数据，所以条数可能不一致）
             1349,《这是一个被改过的 book》,8.9,10000000000000000000000000000000000000, Jimmy Lin / Chris Dyer ,  Morgan and Claypool Publishers / 2010-4-30 / USD 40.00
             2,《Graphical Models Exponential Families and Variational Inference》,9.7,20, Martin J Wainwright / Michael I Jordan ,  Now Publishers Inc / December 16 2008 / USD 125.00
             111,《数据之魅》,7.9,51, （美）Philipp K. Janert / 黄权 ,  清华大学出版社 / 2012-7 / 89.00元
             214,《信用风险评分卡研究》,0,0, 马杜姆.雷法特 / 王松奇 / 林智乾 ,  社会科学文献出版社 / 2013-7 / 58.00
             153,《Recommender Systems》,7.6,17, Dietmar Jannach / Markus Zanker / Alexander Felfernig / Gerhard Friedrich ,  Cambridge University Press / 2010-9-30 / USD 65.00
             159,《这是一个被改过的 book》,7.5,10000000000000000000000000000000000000, Haralambos Marmanis / Dmitry Babenko / 阿稳 / 陈钢 ,  电子工业出版社 / 2011-11 / 65.00元
             60,《利用Python进行数据分析》,8.6,70, Wes McKinney / 唐学韬 ,  机械工业出版社 / 2013-11-18 / 89.00
             93,《Doing Data Science》,8.1,21, Rachel Schutt / Cathy O'Neil ,  O'Reilly Media / 2013-10-30 / USD 39.99
             335,《Understanding Computational Bayesian Statistics》,0,0, , Bolstad William M. / 2009-12 / 918.00元
             355,《Data Analytics》,0,0, Runkler Thomas ,  Springer Fachmedien Wiesbaden / 2012-9 / $ 45.14
             262,《这是一个被改过的 book》,0,10000000000000000000000000000000000000, , 陆旭 / 2008-12 / 20.00元
             182,《大嘴巴漫谈数据挖掘（全彩）》,7.3,28, 易向军 ,  电子工业出版社 / 2014-4 / 69.00元
             102,《神经网络原理》,8,46, Simon Haykin / 叶世伟 / 史忠植 ,  机械工业出版社 / 2004-1 / 69.00元
             319,《Nearest-Neighbor Methods in Learning and Vision》,0,0, Shakhnarovich Gregory (EDT)/ Darrell Trevor (EDT)/ Indyk Piotr (EDT) ,  Mit Pr / 2006-3 / $ 50.85
             49,《这是一个被改过的 book》,8.9,10000000000000000000000000000000000000, Jimmy Lin / Chris Dyer ,  Morgan and Claypool Publishers / 2010-4-30 / USD 40.00
             243,《这是一个被改过的 book》,0,10000000000000000000000000000000000000, Efron Bradley ,  Cambridge University Press / 2010-9 / 646.00元
             345,《模式识别中的核方法及其应用》,0,0, , 2010-2 / 28.00元
             253,《Probabilistic Reasoning in Intelligent Systems》,0,0, Judea Pearl ,  Morgan Kaufmann / 1988-09-15 / USD 106.00
             195,《走进搜索引擎》,6.9,95, , 梁斌 / 2007-1 / 49.80元
             199,《New Internet》,6.6,27, 谭磊 ,  电子工业出版社 / 2013-3 / 69.00元
             238,《这是一个被改过的 book》,0,10000000000000000000000000000000000000, Larry Wasserman ,  Springer / 2010-12-2 / USD 99.00
             96,《模式分析的核方法》,8.1,25, 肖-泰勒 / 克瑞斯天尼 ,  机械工业出版社 / 2006-1 / 48.0
             68,《机器学习(英文版)》,8.5,20, Tom M.Mitchell / 曾华军 ,  机械工业出版社 / 2003-03 / 58.0
             116,《Statistical Models》,7.9,10, David A. Freedman ,  Cambridge University Press / 2009-04-27 / USD 40.00
             371,《Handbook of Latent Semantic Analysis》,0,0, Thomas K. Landauer / Danielle S. McNamara / Simon Dennis / Walter Kintsch ,  Lawrence Erlbaum / 2007-02-15 / USD 99.00
             66,《Learning OpenCV》,8.5,165, Adrian Kaehler / Dr. Gary Rost Bradski ,  oreilly / 2008 / USD 49.99
             121,《大数据》,7.8,311, Anand Rajaraman / Jeffrey David Ullman / 王斌 ,  人民邮电出版社 / 2012-9 / 59.00元
             241,《Machine Learning》,0,0, Peter Flach ,  Cambridge University Press / 2012-11-12 / USD 60.00
             342,《Estimation of Dependences Based on Empirical Data》,0,0, Vladimir Vapnik / Kotz S. ,  Springer / 2006-03-28 / USD 69.95
             39,《这是一个被改过的 book》,9,10000000000000000000000000000000000000, Christopher D. Manning / Prabhakar Raghavan / Hinrich Schütze ,  Cambridge University Press / 2008 / $60.00
             78,《Machine Learning in Action》,8.3,110, Peter Harrington ,  Manning Publications / 2012-4-16 / GBP 29.99
             124,《数据挖掘实用机器学习技术》,7.8,142, Ian H.Witten / Eibe Frank / 董琳 / 邱泉 / 于晓峰 ,  机械工业出版社 / 2006-3 / 48.00元
             147,《神经网络》,7.7,24, [印度]Satish Kumar ,  清华大学出版社 / 2006-8 / 73.00元
             294,《多元统计分析导论》,0,0, (美)T.W.Anderson / 张润楚 程轶 ,  人民邮电出版社 / 2010 年12月 / 89.00元
             276,《Deep Learning》,0,0, , Ohlsson Stellan / 2011-1 / $ 135.60
             256,《Introduction to Pattern Recognition》,0,0, Sergios Theodoridis / Aggelos Pikrakis / Konstantinos Koutroumbas / Dionisis Cavouras ,  Academic Press / 2010-3-31 / USD 41.95
             179,《Python计算机视觉编程》,7.3,10, [瑞典] Jan Erik Solem / 朱文涛 / 袁勇 ,  人民邮电出版社 / 2014-6-10 / 69.00
             202,《图解机器学习》,0,0, 杉山将 / 许永伟 ,  人民邮电出版社 / 2015-4 / 49
        
        
        
        ====== 4. 更新 id = 256 的 book =======
        改前：276,《Deep Learning》,0,0, , Ohlsson Stellan / 2011-1 / $ 135.60
        改后：276,《这是一个被改过的 book》,0,10000000000000000000000000000000000000, , Ohlsson Stellan / 2011-1 / $ 135.60
        
        ==>文件中的结果（因为原文件有数据，所以条数可能不一致）
             1349,《这是一个被改过的 book》,8.9,10000000000000000000000000000000000000, Jimmy Lin / Chris Dyer ,  Morgan and Claypool Publishers / 2010-4-30 / USD 40.00
             2,《Graphical Models Exponential Families and Variational Inference》,9.7,20, Martin J Wainwright / Michael I Jordan ,  Now Publishers Inc / December 16 2008 / USD 125.00
             111,《数据之魅》,7.9,51, （美）Philipp K. Janert / 黄权 ,  清华大学出版社 / 2012-7 / 89.00元
             214,《信用风险评分卡研究》,0,0, 马杜姆.雷法特 / 王松奇 / 林智乾 ,  社会科学文献出版社 / 2013-7 / 58.00
             153,《Recommender Systems》,7.6,17, Dietmar Jannach / Markus Zanker / Alexander Felfernig / Gerhard Friedrich ,  Cambridge University Press / 2010-9-30 / USD 65.00
             159,《这是一个被改过的 book》,7.5,10000000000000000000000000000000000000, Haralambos Marmanis / Dmitry Babenko / 阿稳 / 陈钢 ,  电子工业出版社 / 2011-11 / 65.00元
             60,《利用Python进行数据分析》,8.6,70, Wes McKinney / 唐学韬 ,  机械工业出版社 / 2013-11-18 / 89.00
             93,《Doing Data Science》,8.1,21, Rachel Schutt / Cathy O'Neil ,  O'Reilly Media / 2013-10-30 / USD 39.99
             335,《Understanding Computational Bayesian Statistics》,0,0, , Bolstad William M. / 2009-12 / 918.00元
             355,《Data Analytics》,0,0, Runkler Thomas ,  Springer Fachmedien Wiesbaden / 2012-9 / $ 45.14
             262,《这是一个被改过的 book》,0,10000000000000000000000000000000000000, , 陆旭 / 2008-12 / 20.00元
             182,《大嘴巴漫谈数据挖掘（全彩）》,7.3,28, 易向军 ,  电子工业出版社 / 2014-4 / 69.00元
             102,《神经网络原理》,8,46, Simon Haykin / 叶世伟 / 史忠植 ,  机械工业出版社 / 2004-1 / 69.00元
             319,《Nearest-Neighbor Methods in Learning and Vision》,0,0, Shakhnarovich Gregory (EDT)/ Darrell Trevor (EDT)/ Indyk Piotr (EDT) ,  Mit Pr / 2006-3 / $ 50.85
             49,《这是一个被改过的 book》,8.9,10000000000000000000000000000000000000, Jimmy Lin / Chris Dyer ,  Morgan and Claypool Publishers / 2010-4-30 / USD 40.00
             243,《这是一个被改过的 book》,0,10000000000000000000000000000000000000, Efron Bradley ,  Cambridge University Press / 2010-9 / 646.00元
             345,《模式识别中的核方法及其应用》,0,0, , 2010-2 / 28.00元
             253,《Probabilistic Reasoning in Intelligent Systems》,0,0, Judea Pearl ,  Morgan Kaufmann / 1988-09-15 / USD 106.00
             195,《走进搜索引擎》,6.9,95, , 梁斌 / 2007-1 / 49.80元
             199,《New Internet》,6.6,27, 谭磊 ,  电子工业出版社 / 2013-3 / 69.00元
             238,《这是一个被改过的 book》,0,10000000000000000000000000000000000000, Larry Wasserman ,  Springer / 2010-12-2 / USD 99.00
             96,《模式分析的核方法》,8.1,25, 肖-泰勒 / 克瑞斯天尼 ,  机械工业出版社 / 2006-1 / 48.0
             68,《机器学习(英文版)》,8.5,20, Tom M.Mitchell / 曾华军 ,  机械工业出版社 / 2003-03 / 58.0
             116,《Statistical Models》,7.9,10, David A. Freedman ,  Cambridge University Press / 2009-04-27 / USD 40.00
             371,《Handbook of Latent Semantic Analysis》,0,0, Thomas K. Landauer / Danielle S. McNamara / Simon Dennis / Walter Kintsch ,  Lawrence Erlbaum / 2007-02-15 / USD 99.00
             66,《Learning OpenCV》,8.5,165, Adrian Kaehler / Dr. Gary Rost Bradski ,  oreilly / 2008 / USD 49.99
             121,《大数据》,7.8,311, Anand Rajaraman / Jeffrey David Ullman / 王斌 ,  人民邮电出版社 / 2012-9 / 59.00元
             241,《Machine Learning》,0,0, Peter Flach ,  Cambridge University Press / 2012-11-12 / USD 60.00
             342,《Estimation of Dependences Based on Empirical Data》,0,0, Vladimir Vapnik / Kotz S. ,  Springer / 2006-03-28 / USD 69.95
             39,《这是一个被改过的 book》,9,10000000000000000000000000000000000000, Christopher D. Manning / Prabhakar Raghavan / Hinrich Schütze ,  Cambridge University Press / 2008 / $60.00
             78,《Machine Learning in Action》,8.3,110, Peter Harrington ,  Manning Publications / 2012-4-16 / GBP 29.99
             124,《数据挖掘实用机器学习技术》,7.8,142, Ian H.Witten / Eibe Frank / 董琳 / 邱泉 / 于晓峰 ,  机械工业出版社 / 2006-3 / 48.00元
             147,《神经网络》,7.7,24, [印度]Satish Kumar ,  清华大学出版社 / 2006-8 / 73.00元
             294,《多元统计分析导论》,0,0, (美)T.W.Anderson / 张润楚 程轶 ,  人民邮电出版社 / 2010 年12月 / 89.00元
             276,《这是一个被改过的 book》,0,10000000000000000000000000000000000000, , Ohlsson Stellan / 2011-1 / $ 135.60
             256,《Introduction to Pattern Recognition》,0,0, Sergios Theodoridis / Aggelos Pikrakis / Konstantinos Koutroumbas / Dionisis Cavouras ,  Academic Press / 2010-3-31 / USD 41.95
             179,《Python计算机视觉编程》,7.3,10, [瑞典] Jan Erik Solem / 朱文涛 / 袁勇 ,  人民邮电出版社 / 2014-6-10 / 69.00
             202,《图解机器学习》,0,0, 杉山将 / 许永伟 ,  人民邮电出版社 / 2015-4 / 49
        
        
        
        ====== 5. 查询 book =======
        查询已经存在的书籍 id = 256
        256,《Introduction to Pattern Recognition》,0,0, Sergios Theodoridis / Aggelos Pikrakis / Konstantinos Koutroumbas / Dionisis Cavouras ,  Academic Press / 2010-3-31 / USD 41.95
        查询没有的数据 id = 1000
        None
        
        
        
        ====== 6. 查询 book，并当作对象取值 =======
        查询已经存在的书籍 id = 256
        book.book_id:  256
        book.book_name:  《Introduction to Pattern Recognition》
        book.book_mark:  0
        book.book_count_mark_people:  0
        book.book_author:   Sergios Theodoridis / Aggelos Pikrakis / Konstantinos Koutroumbas / Dionisis Cavouras 
        book.book_publish:    Academic Press / 2010-3-31 / USD 41.95
        
        ====== 按任意键退出 ======
        
        
        Process finished with exit code 0
    
       ```
