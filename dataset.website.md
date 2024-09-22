```python
import streamlit as st
import pandas as pd

dataset = pd.read_excel("ratio_analysis.xlsx")
st.dataframe(dataset)

```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    Cell In[3], line 4
          1 import streamlit as st
          2 import pandas as pd
    ----> 4 dataset = pd.read_excel("ratio_analysis.xlsx")
          5 st.dataframe(dataset)
    

    File D:\Anaconda 3\Lib\site-packages\pandas\util\_decorators.py:211, in deprecate_kwarg.<locals>._deprecate_kwarg.<locals>.wrapper(*args, **kwargs)
        209     else:
        210         kwargs[new_arg_name] = new_arg_value
    --> 211 return func(*args, **kwargs)
    

    File D:\Anaconda 3\Lib\site-packages\pandas\util\_decorators.py:331, in deprecate_nonkeyword_arguments.<locals>.decorate.<locals>.wrapper(*args, **kwargs)
        325 if len(args) > num_allow_args:
        326     warnings.warn(
        327         msg.format(arguments=_format_argument_list(allow_args)),
        328         FutureWarning,
        329         stacklevel=find_stack_level(),
        330     )
    --> 331 return func(*args, **kwargs)
    

    File D:\Anaconda 3\Lib\site-packages\pandas\io\excel\_base.py:482, in read_excel(io, sheet_name, header, names, index_col, usecols, squeeze, dtype, engine, converters, true_values, false_values, skiprows, nrows, na_values, keep_default_na, na_filter, verbose, parse_dates, date_parser, thousands, decimal, comment, skipfooter, convert_float, mangle_dupe_cols, storage_options)
        480 if not isinstance(io, ExcelFile):
        481     should_close = True
    --> 482     io = ExcelFile(io, storage_options=storage_options, engine=engine)
        483 elif engine and engine != io.engine:
        484     raise ValueError(
        485         "Engine should not be specified when passing "
        486         "an ExcelFile - ExcelFile already has the engine set"
        487     )
    

    File D:\Anaconda 3\Lib\site-packages\pandas\io\excel\_base.py:1652, in ExcelFile.__init__(self, path_or_buffer, engine, storage_options)
       1650     ext = "xls"
       1651 else:
    -> 1652     ext = inspect_excel_format(
       1653         content_or_path=path_or_buffer, storage_options=storage_options
       1654     )
       1655     if ext is None:
       1656         raise ValueError(
       1657             "Excel file format cannot be determined, you must specify "
       1658             "an engine manually."
       1659         )
    

    File D:\Anaconda 3\Lib\site-packages\pandas\io\excel\_base.py:1525, in inspect_excel_format(content_or_path, storage_options)
       1522 if isinstance(content_or_path, bytes):
       1523     content_or_path = BytesIO(content_or_path)
    -> 1525 with get_handle(
       1526     content_or_path, "rb", storage_options=storage_options, is_text=False
       1527 ) as handle:
       1528     stream = handle.handle
       1529     stream.seek(0)
    

    File D:\Anaconda 3\Lib\site-packages\pandas\io\common.py:865, in get_handle(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)
        856         handle = open(
        857             handle,
        858             ioargs.mode,
       (...)
        861             newline="",
        862         )
        863     else:
        864         # Binary mode
    --> 865         handle = open(handle, ioargs.mode)
        866     handles.append(handle)
        868 # Convert BytesIO or file objects passed with an encoding
    

    FileNotFoundError: [Errno 2] No such file or directory: 'ratio_analysis.xlsx'



```python

```
