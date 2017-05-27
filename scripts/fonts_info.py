# coding=utf-8

font_files = {
              "cambria.ttc": ("ws"),
              "consola.ttf": ("ws"),
              "cour.ttf": ("ws"),
              "segoeui.ttf": ("ws"),
              "tahoma.ttf": ("ws"),
              "seguisym.ttf": ("mo"),
              "symbola.ttf": ("mo"),
              "STIX2Math.otf": ("mo"),
              # "simkai.ttf": ("sc", "tc", "hk"),
              # "simfang.ttf": ("sc", "tc", "hk"),
              # "simsun.ttc": ("sc", "tc", "hk"),
              # "msyh.ttc": ("sc", "tc", "hk"),
              # "mingliu.ttc": ("tc", "hk"),
              # "msjh.ttc": ("tc", "hk"),
              # "msjhbd.ttc": ("tc", "hk"),
              # "kaiu.ttf": ("tc", "hk"),
              # "batang.ttc": ("kr"),
              # "malgun.ttf": ("kr"),
              # "malgunbd.ttf": ("kr"),
              # "malgunsl.ttf": ("kr"),
              # "meiryo.ttc": ("jc", "jp"),
              # "meiryob.ttc": ("jc", "jp"),
              # "msmincho.ttc": ("jc", "jp"),
              # "YuGothR.ttc": ("jc", "jp"),
              # "YuGothB.ttc": ("jc", "jp"),
              }

# note:
#   latinmodern-math.otf misses a lots of chars, so will not use

# some fonts need special treatment
# for example, msyh.ttc shifted down, we need to adjust it up
y_shift = {"cambria": -5,
           "consola": 10,
           "cour": -5,
           "segoeui": -10,
           "tahoma": 0,
           "STIX2Math": 5,
           "seguisym": -10,
           "msyh": -20,
           "msjh": -19,
           "msjhbd": -19,
           "meiryo": -17,
           "meiryob": -17,
           "malgun": -18,
           "malgunbd": -18,
           "malgunsl": -18,
           "cambria.ttc": -10,
           }
