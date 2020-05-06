import flopy as fp
import glob
import os
import sys


class InowasModflowReadAdapter:
    _ws = None

    _mf = None

    def __init__(self):
        pass

    @staticmethod
    def load(path):

        abspath = os.path.abspath(os.path.join(path))
        if not os.path.exists(abspath):
            raise FileNotFoundError('Path not found: ' + path)

        if len(glob.glob1(abspath, "*.nam")) == 0 and len(glob.glob1(abspath, "*.mfn")) == 0:
            raise FileNotFoundError('Modflow name file with ending .nam or .mfn not found')

        orig_stdout = sys.stdout
        f = open(os.path.join(abspath, 'load.log'), 'w')
        sys.stdout = f

        instance = InowasModflowReadAdapter()
        instance._ws = path

        name_file = ''
        if len(glob.glob1(abspath, "*.nam")) > 0:
            name_file = glob.glob1(abspath, "*.nam")[0]

        if len(glob.glob1(abspath, "*.mfn")) > 0:
            name_file = glob.glob1(abspath, "*.mfn")[0]

        try:
            instance._mf = fp.modflow.Modflow.load(
                os.path.join(abspath, name_file),
                check=True,
                forgive=True,
                model_ws=abspath,
                verbose=True,
            )

            sys.stdout = orig_stdout
            f.close()

            return instance

        except:
            sys.stdout = orig_stdout
            f.close()
            raise
