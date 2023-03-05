import json
import tempfile
from autoviz.AutoViz_Class import AutoViz_Class


class AutoVizService:
    def __init__(self, json_data):
        tfile = tempfile.NamedTemporaryFile(mode="w+")
        json.dump(json_data, tfile)
        tfile.flush()
        self.data_path = tfile.name

    def generate_html(self):
        AV = AutoViz_Class()

        dft = AV.AutoViz(
            self.data_path ,
            sep=",",
            depVar="",
            dfte=None,
            header=0,
            verbose=0,
            lowess=False,
            chart_format="html",
            max_rows_analyzed=150000,
            max_cols_analyzed=30,
            save_plot_dir=None
        )
        # import pdb;pdb.set_trace()
        return dft
