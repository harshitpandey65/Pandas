Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
>>> import pandas as pd
>>> df=pd.read_csv('C:\Users\harsh\OneDrive\Desktop\creditcard.csv')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> df=pd.read_csv(r'C:\Users\harsh\OneDrive\Desktop\creditcard.csv')
>>> print(df.head())
   Time        V1        V2        V3  ...       V27       V28  Amount  Class
0   0.0 -1.359807 -0.072781  2.536347  ...  0.133558 -0.021053  149.62      0
1   0.0  1.191857  0.266151  0.166480  ... -0.008983  0.014724    2.69      0
2   1.0 -1.358354 -1.340163  1.773209  ... -0.055353 -0.059752  378.66      0
3   1.0 -0.966272 -0.185226  1.792993  ...  0.062723  0.061458  123.50      0
4   2.0 -1.158233  0.877737  1.548718  ...  0.219422  0.215153   69.99      0

[5 rows x 31 columns]
>>> df.info
<bound method DataFrame.info of             Time         V1         V2  ...       V28  Amount  Class
0            0.0  -1.359807  -0.072781  ... -0.021053  149.62      0
1            0.0   1.191857   0.266151  ...  0.014724    2.69      0
2            1.0  -1.358354  -1.340163  ... -0.059752  378.66      0
3            1.0  -0.966272  -0.185226  ...  0.061458  123.50      0
4            2.0  -1.158233   0.877737  ...  0.215153   69.99      0
...          ...        ...        ...  ...       ...     ...    ...
284802  172786.0 -11.881118  10.071785  ...  0.823731    0.77      0
284803  172787.0  -0.732789  -0.055080  ... -0.053527   24.79      0
284804  172788.0   1.919565  -0.301254  ... -0.026561   67.88      0
284805  172788.0  -0.240440   0.530483  ...  0.104533   10.00      0
284806  172792.0  -0.533413  -0.189733  ...  0.013649  217.00      0

[284807 rows x 31 columns]>
>>> print(df.info())
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 284807 entries, 0 to 284806
Data columns (total 31 columns):
 #   Column  Non-Null Count   Dtype  
---  ------  --------------   -----  
 0   Time    284807 non-null  float64
 1   V1      284807 non-null  float64
 2   V2      284807 non-null  float64
 3   V3      284807 non-null  float64
 4   V4      284807 non-null  float64
 5   V5      284807 non-null  float64
 6   V6      284807 non-null  float64
 7   V7      284807 non-null  float64
 8   V8      284807 non-null  float64
 9   V9      284807 non-null  float64
 10  V10     284807 non-null  float64
 11  V11     284807 non-null  float64
 12  V12     284807 non-null  float64
 13  V13     284807 non-null  float64
 14  V14     284807 non-null  float64
 15  V15     284807 non-null  float64
 16  V16     284807 non-null  float64
 17  V17     284807 non-null  float64
 18  V18     284807 non-null  float64
 19  V19     284807 non-null  float64
 20  V20     284807 non-null  float64
 21  V21     284807 non-null  float64
 22  V22     284807 non-null  float64
 23  V23     284807 non-null  float64
 24  V24     284807 non-null  float64
 25  V25     284807 non-null  float64
 26  V26     284807 non-null  float64
 27  V27     284807 non-null  float64
 28  V28     284807 non-null  float64
 29  Amount  284807 non-null  float64
 30  Class   284807 non-null  int64  
dtypes: float64(30), int64(1)
memory usage: 67.4 MB
None
print(df.isnull)
<bound method DataFrame.isnull of             Time         V1         V2  ...       V28  Amount  Class
0            0.0  -1.359807  -0.072781  ... -0.021053  149.62      0
1            0.0   1.191857   0.266151  ...  0.014724    2.69      0
2            1.0  -1.358354  -1.340163  ... -0.059752  378.66      0
3            1.0  -0.966272  -0.185226  ...  0.061458  123.50      0
4            2.0  -1.158233   0.877737  ...  0.215153   69.99      0
...          ...        ...        ...  ...       ...     ...    ...
284802  172786.0 -11.881118  10.071785  ...  0.823731    0.77      0
284803  172787.0  -0.732789  -0.055080  ... -0.053527   24.79      0
284804  172788.0   1.919565  -0.301254  ... -0.026561   67.88      0
284805  172788.0  -0.240440   0.530483  ...  0.104533   10.00      0
284806  172792.0  -0.533413  -0.189733  ...  0.013649  217.00      0

[284807 rows x 31 columns]>
print(df.isnull())
         Time     V1     V2     V3     V4  ...    V26    V27    V28  Amount  Class
0       False  False  False  False  False  ...  False  False  False   False  False
1       False  False  False  False  False  ...  False  False  False   False  False
2       False  False  False  False  False  ...  False  False  False   False  False
3       False  False  False  False  False  ...  False  False  False   False  False
4       False  False  False  False  False  ...  False  False  False   False  False
...       ...    ...    ...    ...    ...  ...    ...    ...    ...     ...    ...
284802  False  False  False  False  False  ...  False  False  False   False  False
284803  False  False  False  False  False  ...  False  False  False   False  False
284804  False  False  False  False  False  ...  False  False  False   False  False
284805  False  False  False  False  False  ...  False  False  False   False  False
284806  False  False  False  False  False  ...  False  False  False   False  False

[284807 rows x 31 columns]
print(df.describe())
                Time            V1  ...         Amount          Class
count  284807.000000  2.848070e+05  ...  284807.000000  284807.000000
mean    94813.859575  1.175161e-15  ...      88.349619       0.001727
std     47488.145955  1.958696e+00  ...     250.120109       0.041527
min         0.000000 -5.640751e+01  ...       0.000000       0.000000
25%     54201.500000 -9.203734e-01  ...       5.600000       0.000000
50%     84692.000000  1.810880e-02  ...      22.000000       0.000000
75%    139320.500000  1.315642e+00  ...      77.165000       0.000000
max    172792.000000  2.454930e+00  ...   25691.160000       1.000000

[8 rows x 31 columns]
df.isnull()
         Time     V1     V2     V3     V4  ...    V26    V27    V28  Amount  Class
0       False  False  False  False  False  ...  False  False  False   False  False
1       False  False  False  False  False  ...  False  False  False   False  False
2       False  False  False  False  False  ...  False  False  False   False  False
3       False  False  False  False  False  ...  False  False  False   False  False
4       False  False  False  False  False  ...  False  False  False   False  False
...       ...    ...    ...    ...    ...  ...    ...    ...    ...     ...    ...
284802  False  False  False  False  False  ...  False  False  False   False  False
284803  False  False  False  False  False  ...  False  False  False   False  False
284804  False  False  False  False  False  ...  False  False  False   False  False
284805  False  False  False  False  False  ...  False  False  False   False  False
284806  False  False  False  False  False  ...  False  False  False   False  False

[284807 rows x 31 columns]
df.size()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    df.size()
TypeError: 'int' object is not callable
df.size
8829017
df.shape
(284807, 31)
df,isnll.sum
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    df,isnll.sum
NameError: name 'isnll' is not defined
df.isnll.sum()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    df.isnll.sum()
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\generic.py", line 6321, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'isnll'. Did you mean: 'isnull'?
df.isnull.sum()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    df.isnull.sum()
AttributeError: 'function' object has no attribute 'sum'
df.isnull().sum()
Time      0
V1        0
V2        0
V3        0
V4        0
V5        0
V6        0
V7        0
V8        0
V9        0
V10       0
V11       0
V12       0
V13       0
V14       0
V15       0
V16       0
V17       0
V18       0
V19       0
V20       0
V21       0
V22       0
V23       0
V24       0
V25       0
V26       0
V27       0
V28       0
Amount    0
Class     0
dtype: int64
df.duplicated()
0         False
1         False
2         False
3         False
4         False
          ...  
284802    False
284803    False
284804    False
284805    False
284806    False
Length: 284807, dtype: bool
print(df.duplicated().sum())
1081
print(df.columns)
Index(['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
       'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
       'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount',
       'Class'],
      dtype='object')
print('extract the coulumns')
extract the coulumns
df1=df[['V1','V2','V3','V4','V5']]
print(df1.head())
         V1        V2        V3        V4        V5
0 -1.359807 -0.072781  2.536347  1.378155 -0.338321
1  1.191857  0.266151  0.166480  0.448154  0.060018
2 -1.358354 -1.340163  1.773209  0.379780 -0.503198
3 -0.966272 -0.185226  1.792993 -0.863291 -0.010309
4 -1.158233  0.877737  1.548718  0.403034 -0.407193
df1.head()
         V1        V2        V3        V4        V5
0 -1.359807 -0.072781  2.536347  1.378155 -0.338321
1  1.191857  0.266151  0.166480  0.448154  0.060018
2 -1.358354 -1.340163  1.773209  0.379780 -0.503198
3 -0.966272 -0.185226  1.792993 -0.863291 -0.010309
4 -1.158233  0.877737  1.548718  0.403034 -0.407193
df.isnull()
         Time     V1     V2     V3     V4  ...    V26    V27    V28  Amount  Class
0       False  False  False  False  False  ...  False  False  False   False  False
1       False  False  False  False  False  ...  False  False  False   False  False
2       False  False  False  False  False  ...  False  False  False   False  False
3       False  False  False  False  False  ...  False  False  False   False  False
4       False  False  False  False  False  ...  False  False  False   False  False
...       ...    ...    ...    ...    ...  ...    ...    ...    ...     ...    ...
284802  False  False  False  False  False  ...  False  False  False   False  False
284803  False  False  False  False  False  ...  False  False  False   False  False
284804  False  False  False  False  False  ...  False  False  False   False  False
284805  False  False  False  False  False  ...  False  False  False   False  False
284806  False  False  False  False  False  ...  False  False  False   False  False

[284807 rows x 31 columns]
df1.isnull()
           V1     V2     V3     V4     V5
0       False  False  False  False  False
1       False  False  False  False  False
2       False  False  False  False  False
3       False  False  False  False  False
4       False  False  False  False  False
...       ...    ...    ...    ...    ...
284802  False  False  False  False  False
284803  False  False  False  False  False
284804  False  False  False  False  False
284805  False  False  False  False  False
284806  False  False  False  False  False

[284807 rows x 5 columns]
df1.isnul().sum()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    df1.isnul().sum()
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\generic.py", line 6321, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'isnul'. Did you mean: 'isnull'?
df1.isnull().sum()
V1    0
V2    0
V3    0
V4    0
V5    0
dtype: int64
import numpy as np
import pandas as pd
import matplotlib.pylib
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    import matplotlib.pylib
ModuleNotFoundError: No module named 'matplotlib.pylib'
df.Amount['V1'].value_counts()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    df.Amount['V1'].value_counts()
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\series.py", line 1133, in __getitem__
    return self._get_value(key)
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\series.py", line 1249, in _get_value
    loc = self.index.get_loc(label)
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\range.py", line 417, in get_loc
    raise KeyError(key)
KeyError: 'V1'
df['V1'].value_counts()
V1
 1.245674     77
 2.055797     77
 2.053311     62
 1.302378     60
 2.040211     53
              ..
-11.881118     1
-0.732789      1
 1.919565      1
-0.240440      1
-0.425966      1
Name: count, Length: 275663, dtype: int64
print('concatenate')
concatenate
d1={'empid':['e5651','e5652','e5643','e5652','e5655']}
print(d1)
{'empid': ['e5651', 'e5652', 'e5643', 'e5652', 'e5655']}
d1={'empid':['e5651','e5652','e5643','e5652','e5655'],'name':['payal','advina','madan','rafel','gopal'],'location':['pune','banglore','banglore','chennai','chennai'],'age,':[35,30,45,40,32]}
d2={'empid':['e4501','e4502','e5643','e4503'],'name':['sumit','nikhil','paul'],'location':['mumbai','mumbai','banglore'],'age,':[35,30,45]}
d3={'year of service':[10,5,17,12,7]}
emp1=pf.DataFrame(d1)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    emp1=pf.DataFrame(d1)
NameError: name 'pf' is not defined. Did you mean: 'pd'?
emp1=pd.DataFrame(d1)
emp2=pd.DataFrame(d2)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    emp2=pd.DataFrame(d2)
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\frame.py", line 782, in __init__
    mgr = dict_to_mgr(data, index, columns, dtype=dtype, copy=copy, typ=manager)
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\internals\construction.py", line 503, in dict_to_mgr
    return arrays_to_mgr(arrays, columns, index, dtype=dtype, typ=typ, consolidate=copy)
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\internals\construction.py", line 114, in arrays_to_mgr
    index = _extract_index(arrays)
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\internals\construction.py", line 677, in _extract_index
    raise ValueError("All arrays must be of the same length")
ValueError: All arrays must be of the same length
emp2=pd.DataFrame(d2)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    emp2=pd.DataFrame(d2)
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\frame.py", line 782, in __init__
    mgr = dict_to_mgr(data, index, columns, dtype=dtype, copy=copy, typ=manager)
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\internals\construction.py", line 503, in dict_to_mgr
    return arrays_to_mgr(arrays, columns, index, dtype=dtype, typ=typ, consolidate=copy)
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\internals\construction.py", line 114, in arrays_to_mgr
    index = _extract_index(arrays)
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\internals\construction.py", line 677, in _extract_index
    raise ValueError("All arrays must be of the same length")
ValueError: All arrays must be of the same length
emp1=pd.DataFrame(d2)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    emp1=pd.DataFrame(d2)
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\frame.py", line 782, in __init__
    mgr = dict_to_mgr(data, index, columns, dtype=dtype, copy=copy, typ=manager)
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\internals\construction.py", line 503, in dict_to_mgr
    return arrays_to_mgr(arrays, columns, index, dtype=dtype, typ=typ, consolidate=copy)
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\internals\construction.py", line 114, in arrays_to_mgr
    index = _extract_index(arrays)
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\internals\construction.py", line 677, in _extract_index
    raise ValueError("All arrays must be of the same length")
ValueError: All arrays must be of the same length
d2={'empid':['e4501','e4502','e5643','e4503'],'name':['sumit','nikhil','paul'],'location':['mumbai','mumbai','banglore']}
emp1=pd.DataFrame(d2)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    emp1=pd.DataFrame(d2)
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\frame.py", line 782, in __init__
    mgr = dict_to_mgr(data, index, columns, dtype=dtype, copy=copy, typ=manager)
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\internals\construction.py", line 503, in dict_to_mgr
    return arrays_to_mgr(arrays, columns, index, dtype=dtype, typ=typ, consolidate=copy)
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\internals\construction.py", line 114, in arrays_to_mgr
    index = _extract_index(arrays)
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\internals\construction.py", line 677, in _extract_index
    raise ValueError("All arrays must be of the same length")
ValueError: All arrays must be of the same length
emp2=pd.DataFrame(d2)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    emp2=pd.DataFrame(d2)
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\frame.py", line 782, in __init__
    mgr = dict_to_mgr(data, index, columns, dtype=dtype, copy=copy, typ=manager)
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\internals\construction.py", line 503, in dict_to_mgr
    return arrays_to_mgr(arrays, columns, index, dtype=dtype, typ=typ, consolidate=copy)
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\internals\construction.py", line 114, in arrays_to_mgr
    index = _extract_index(arrays)
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\internals\construction.py", line 677, in _extract_index
    raise ValueError("All arrays must be of the same length")
ValueError: All arrays must be of the same length
emp1=pld.DataFrame(d1)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    emp1=pld.DataFrame(d1)
NameError: name 'pld' is not defined. Did you mean: 'pd'?
emp1=pd.DataFrame(d1)
emp2=pd.DataFrame(d2)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    emp2=pd.DataFrame(d2)
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\frame.py", line 782, in __init__
    mgr = dict_to_mgr(data, index, columns, dtype=dtype, copy=copy, typ=manager)
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\internals\construction.py", line 503, in dict_to_mgr
    return arrays_to_mgr(arrays, columns, index, dtype=dtype, typ=typ, consolidate=copy)
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\internals\construction.py", line 114, in arrays_to_mgr
    index = _extract_index(arrays)
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\internals\construction.py", line 677, in _extract_index
    raise ValueError("All arrays must be of the same length")
ValueError: All arrays must be of the same length
d2={'empid':['e4501','e4502','e5643'],'name':['sumit','nikhil','paul'],'location':['mumbai','mumbai','banglore'],'age,':[35,30,45]}
emp2=pd.DataFrame(d2)
service=pd.DataFrame(d3)
print(emp1)
   empid    name  location  age,
0  e5651   payal      pune    35
1  e5652  advina  banglore    30
2  e5643   madan  banglore    45
3  e5652   rafel   chennai    40
4  e5655   gopal   chennai    32
emp2
   empid    name  location  age,
0  e4501   sumit    mumbai    35
1  e4502  nikhil    mumbai    30
2  e5643    paul  banglore    45
service
   year of service
0               10
1                5
2               17
3               12
4                7
emp1
   empid    name  location  age,
0  e5651   payal      pune    35
1  e5652  advina  banglore    30
2  e5643   madan  banglore    45
3  e5652   rafel   chennai    40
4  e5655   gopal   chennai    32
emp1.mode()
   empid    name  location  age,
0  e5652  advina  banglore    30
1    NaN   gopal   chennai    32
2    NaN   madan       NaN    35
3    NaN   payal       NaN    40
4    NaN   rafel       NaN    45
age.mode()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    age.mode()
NameError: name 'age' is not defined
emp1['age']:mode()
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    emp1['age']:mode()
NameError: name 'mode' is not defined
emp1['age']:medium()
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    emp1['age']:medium()
NameError: name 'medium' is not defined
emp1['age'].median()
Traceback (most recent call last):
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py", line 3812, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 167, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 196, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7088, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7096, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'age'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    emp1['age'].median()
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\frame.py", line 4113, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py", line 3819, in get_loc
    raise KeyError(key) from err
KeyError: 'age'
emp1['age'].median()
Traceback (most recent call last):
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py", line 3812, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 167, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 196, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7088, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7096, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'age'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    emp1['age'].median()
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\frame.py", line 4113, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py", line 3819, in get_loc
    raise KeyError(key) from err
KeyError: 'age'
emp1['age'].mean()
Traceback (most recent call last):
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py", line 3812, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 167, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 196, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7088, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7096, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'age'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    emp1['age'].mean()
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\frame.py", line 4113, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py", line 3819, in get_loc
    raise KeyError(key) from err
KeyError: 'age'
emp1['age']:mode()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    emp1['age']:mode()
NameError: name 'mode' is not defined
emp1['age'].meadian()
Traceback (most recent call last):
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py", line 3812, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 167, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 196, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7088, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7096, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'age'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    emp1['age'].meadian()
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\frame.py", line 4113, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py", line 3819, in get_loc
    raise KeyError(key) from err
KeyError: 'age'
service
   year of service
0               10
1                5
2               17
3               12
4                7
    service
    
SyntaxError: unexpected indent
service
   year of service
0               10
1                5
2               17
3               12
4                7
data=pd.concat([emp1,emp2])
print(data)
   empid    name  location  age,
0  e5651   payal      pune    35
1  e5652  advina  banglore    30
2  e5643   madan  banglore    45
3  e5652   rafel   chennai    40
4  e5655   gopal   chennai    32
0  e4501   sumit    mumbai    35
1  e4502  nikhil    mumbai    30
2  e5643    paul  banglore    45
data=pd.concat([emp1,emp2].axis=1)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
data=pd.concat([emp1,emp2].axis===1)
SyntaxError: invalid syntax
data=pd.concat([emp1,emp2],axis==1)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    data=pd.concat([emp1,emp2],axis==1)
NameError: name 'axis' is not defined
data=pd.concat([emp1,emp2],axis=1)
print(data)
   empid    name  location  age,  empid    name  location  age,
0  e5651   payal      pune    35  e4501   sumit    mumbai  35.0
1  e5652  advina  banglore    30  e4502  nikhil    mumbai  30.0
2  e5643   madan  banglore    45  e5643    paul  banglore  45.0
3  e5652   rafel   chennai    40    NaN     NaN       NaN   NaN
4  e5655   gopal   chennai    32    NaN     NaN       NaN   NaN
data=pd.concat([emp1,emp2],axis=1)
data=pd.concat([emp1,service],axis=1)
print(data)
   empid    name  location  age,  year of service
0  e5651   payal      pune    35               10
1  e5652  advina  banglore    30                5
2  e5643   madan  banglore    45               17
3  e5652   rafel   chennai    40               12
4  e5655   gopal   chennai    32                7
data=pd.concat([data,service],axis=1)
print(data)
   empid    name  location  age,  year of service  year of service
0  e5651   payal      pune    35               10               10
1  e5652  advina  banglore    30                5                5
2  e5643   madan  banglore    45               17               17
3  e5652   rafel   chennai    40               12               12
4  e5655   gopal   chennai    32                7                7
data=pd.concat([emp1,emp2])
print(data)
   empid    name  location  age,
0  e5651   payal      pune    35
1  e5652  advina  banglore    30
2  e5643   madan  banglore    45
3  e5652   rafel   chennai    40
4  e5655   gopal   chennai    32
0  e4501   sumit    mumbai    35
1  e4502  nikhil    mumbai    30
2  e5643    paul  banglore    45
data=pd.concat([data,service],axis=1)
print(data)
   empid    name  location  age,  year of service
0  e5651   payal      pune    35               10
1  e5652  advina  banglore    30                5
2  e5643   madan  banglore    45               17
3  e5652   rafel   chennai    40               12
4  e5655   gopal   chennai    32                7
0  e4501   sumit    mumbai    35               10
1  e4502  nikhil    mumbai    30                5
2  e5643    paul  banglore    45               17
data=pd.concat([\emp1,service],axis=0)
SyntaxError: unexpected character after line continuation character
data=pd.concat([emp1,service],axis=0)
print(data)
   empid    name  location  age,  year of service
0  e5651   payal      pune  35.0              NaN
1  e5652  advina  banglore  30.0              NaN
2  e5643   madan  banglore  45.0              NaN
3  e5652   rafel   chennai  40.0              NaN
4  e5655   gopal   chennai  32.0              NaN
0    NaN     NaN       NaN   NaN             10.0
1    NaN     NaN       NaN   NaN              5.0
2    NaN     NaN       NaN   NaN             17.0
3    NaN     NaN       NaN   NaN             12.0
4    NaN     NaN       NaN   NaN              7.0
data.append(emp1)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    data.append(emp1)
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\generic.py", line 6321, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'append'. Did you mean: '_append'?
emp1.data(emp2)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    emp1.data(emp2)
  File "C:\Users\harsh\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\generic.py", line 6321, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'data'. Did you mean: '_data'?
emp1._append(emp2)
   empid    name  location  age,
0  e5651   payal      pune    35
1  e5652  advina  banglore    30
2  e5643   madan  banglore    45
3  e5652   rafel   chennai    40
4  e5655   gopal   chennai    32
0  e4501   sumit    mumbai    35
1  e4502  nikhil    mumbai    30
2  e5643    paul  banglore    45
data=emp1._append(emp2)
print(data)
   empid    name  location  age,
0  e5651   payal      pune    35
1  e5652  advina  banglore    30
2  e5643   madan  banglore    45
3  e5652   rafel   chennai    40
4  e5655   gopal   chennai    32
0  e4501   sumit    mumbai    35
1  e4502  nikhil    mumbai    30
2  e5643    paul  banglore    45
data.isnull()
   empid   name  location   age,
0  False  False     False  False
1  False  False     False  False
2  False  False     False  False
3  False  False     False  False
4  False  False     False  False
0  False  False     False  False
1  False  False     False  False
2  False  False     False  False
data.isnull().sum()
empid       0
name        0
location    0
age,        0
dtype: int64
data=emp2._append(emp1)
print(data)
   empid    name  location  age,
0  e4501   sumit    mumbai    35
1  e4502  nikhil    mumbai    30
2  e5643    paul  banglore    45
0  e5651   payal      pune    35
1  e5652  advina  banglore    30
2  e5643   madan  banglore    45
3  e5652   rafel   chennai    40
4  e5655   gopal   chennai    32
print(data.head())
   empid    name  location  age,
0  e4501   sumit    mumbai    35
1  e4502  nikhil    mumbai    30
2  e5643    paul  banglore    45
0  e5651   payal      pune    35
1  e5652  advina  banglore    30
data.head(3)
   empid    name  location  age,
0  e4501   sumit    mumbai    35
1  e4502  nikhil    mumbai    30
2  e5643    paul  banglore    45
import os
os.getpwd()
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    os.getpwd()
AttributeError: module 'os' has no attribute 'getpwd'. Did you mean: 'getcwd'?
os.getcwd()
'C:\\Users\\harsh\\AppData\\Local\\Programs\\Python\\Python313'
series=pd.Series()
print(type(series))
<class 'pandas.core.series.Series'>
