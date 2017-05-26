# coding=utf-8

font_files = {"simkai.ttf": ("sc", "tc", "hk"),
              "simfang.ttf": ("sc", "tc", "hk"),
              "simsun.ttc": ("sc", "tc", "hk"),
              "msyh.ttc": ("sc", "tc", "hk"),
              "mingliu.ttc": ("tc", "hk"),
              "msjh.ttc": ("tc", "hk"),
              "msjhbd.ttc": ("tc", "hk"),
              "kaiu.ttf": ("tc", "hk"),
              "batang.ttc": ("kr"),
              "malgun.ttf": ("kr"),
              "malgunbd.ttf": ("kr"),
              "malgunsl.ttf": ("kr"),
              "meiryo.ttc": ("jc", "jp"),
              "meiryob.ttc": ("jc", "jp"),
              "msmincho.ttc": ("jc", "jp"),
              "YuGothR.ttc": ("jc", "jp"),
              "YuGothB.ttc": ("jc", "jp"),
              }

# some fonts need special treatment
# for example, msyh.ttc shifted down, we need to adjust it up
y_shift = {"msyh": -20,
           "meiryo": -17,
           "meiryob": -17,
           "malgun": -18,
           "malgunbd": -18,
           "malgunsl": -18,
           }
