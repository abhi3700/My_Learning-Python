# `matplotlib`
## Installation
* `conda install matplotlib`

## Coding
* ### Import 
  ```py
  import matplotlib.pyplot as plt
  ```
* ### Plot `x` vs `y`
  **Code:**
  ```py
  plt.plot([1, 2, 3, 4])
  plt.ylabel('some numbers')
  plt.show()
  ```
  **Description:**
  - `y = [1, 2, 3, 4]`
  - `x = [0, 1, 2, 3]` (by default, starts with '0')
  
* ### Plot `x` vs `y` with both the data
  **Code:**  
  ```py
  plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
  plt.ylabel('square numbers')
  plt.show()
  ```
  **Description:**
  - `x = [1, 2, 3, 4]`
  - `y = [1, 4, 9, 16]`  
  
* ### Plot linestyle, marker, color
  ```py
  plt.plot(df_er["Date (MM/DD/YY)"], df_er["Etch Rate (A/Min)"], linestyle='-', marker='o', color='b')
  ```
  [Reference](https://stackoverflow.com/questions/8409095/matplotlib-set-markers-for-individual-points-on-a-line/8409110#8409110)
  [color codes](https://www.rapidtables.com/web/color/html-color-codes.html)
* ### Date formatting in x-axis
  ```py
  import matplotlib.dates as mdates
  monthyearFmt = mdates.DateFormatter('%Y-%b')          # formatting as 2017-Jan
  ax1.xaxis.set_major_formatter(monthyearFmt)
  _ = plt.xticks(rotation=90)                           # rotating 90 counterclockwise
  ax1.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=MO, interval=2))          # set ticks every 2nd Monday
  ```
  
  [Date picks](https://matplotlib.org/api/dates_api.html#date-tickers)
  ```md
  // Date notation
  %Y - 2017
  %B - January
  %b - Jan
  %d - 21
  ```
  [matplotlib.dates API](https://matplotlib.org/api/dates_api.html) <br/>
  [Refer 1](https://stackoverflow.com/questions/43968985/changing-the-formatting-of-a-datetime-axis-in-matplotlib/43969357#43969357), [Refer 2](https://scentellegher.github.io/programming/2017/05/24/pandas-bar-plot-with-formatted-dates.html)
* ### Major and Minor ticks on the axes
  ```py
  # Major ticks every 20, minor ticks every 5
  major_ticks = np.arange(0, 101, 20)
  minor_ticks = np.arange(0, 101, 5)

  ax.set_xticks(major_ticks)
  ax.set_xticks(minor_ticks, minor=True)
  ax.set_yticks(major_ticks)
  ax.set_yticks(minor_ticks, minor=True)
  ```
  [Reference](https://stackoverflow.com/a/24953575/6774636)
* ### Multiple plots on a single x-axis
  ```py
  plt.plot(df_er["Date (MM/DD/YY)"], df_er["Etch Rate (A/Min)"], linestyle='-', marker='o', markerfacecolor='#008000', color='#FF7F50')    # plot date vs ER
  plt.plot(df_er["Date (MM/DD/YY)"], df_er["LSL"], linestyle='-', color='#0000CD')        # plot date vs LSL
  plt.plot(df_er["Date (MM/DD/YY)"], df_er["LCL"], linestyle='-', color='#FF1493')        # plot date vs LCL 
  plt.plot(df_er["Date (MM/DD/YY)"], df_er["UCL"], linestyle='-', color='#FF1493')        # plot date vs UCL
  ```
* ### Labels font size
  ```py
  import matplotlib.pylab as pylab
  params = {'legend.fontsize': 'x-large',
            'figure.figsize': (15, 5),
           'axes.labelsize': 'x-large',
           'axes.titlesize':'x-large',
           'xtick.labelsize':'x-large',
           'ytick.labelsize':'x-large'}
  pylab.rcParams.update(params)
  ```
  [Reference](https://stackoverflow.com/a/38251497/6774636)
* ### Format string characters description
  [Reference](https://matplotlib.org/2.1.1/api/_as_gen/matplotlib.pyplot.plot.html)
* ### Custom legends
  ```py
  # Custom Legends
  custom_lines = [
      Line2D([0], [0], color='#FF7F50', lw=4),
      Line2D([0], [0], color='#0000CD', lw=4),
      Line2D([0], [0], color='#FF1493', lw=4)        
      ]
  ax_cp.legend(custom_lines, ['CP', 'USL', 'UCL'], fontsize=11)        
  ```
  [Reference](https://matplotlib.org/gallery/text_labels_and_annotations/custom_legends.html)
* ### Annotations on hovering over a plot
  ```py
  from mpldatacursor import datacursor
  df_cp = sht_asfe1_cp.range('A10').options(
          pd.DataFrame, header=1, index=False, expand='table'
          ).value											                # fetch the data from sheet- 'ASFE1-CP'
  df_cp['Remarks'].fillna('NIL', inplace=True)      # replacing the empty cells with 'NIL'
  df_cp = df_cp[["Date (MM/DD/YY)", "delta CP", "USL", "UCL", "Remarks"]]        # The final dataframe with required columns
  lines = ax_cp.plot(df_cp["Date (MM/DD/YY)"], df_cp["delta CP"], visible=False)
  datacursor(lines, hover=True, point_labels=df_cp['Remarks'])
  plt.show()      # this would activate hover 
  ```
  > NOTE: The 'Remarks' column cannot have value as 0 or empty cells. So, fill empty cells with 'NIL'
  
  **References**:
  - [How to show data labels .....](https://stackoverflow.com/questions/21998663/how-to-show-data-labels-when-you-mouse-over-data/22002324#22002324)
  - [Scatter plot with cursor](https://mpld3.github.io/examples/scatter_tooltip.html)
  
  **Packages:**
  - [mpldatacursor](https://anaconda.org/BjornFJohansson/mpldatacursor)  [RECOMMENDED]
  - [mplcursor](https://anaconda.org/conda-forge/mplcursors)  [A FORK of mpldatacursor]
  - [mpld3](https://mpld3.github.io/index.html)
