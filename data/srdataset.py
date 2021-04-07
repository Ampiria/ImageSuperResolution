import os
import glob
import pickle
import random
import numpy as np
import imageio
import torch
import torch.utils.data as data

class SRDataset(data.Dataset):
  def __init__(self, datapath, name='', train=True) -> None:
      self.split = "TRAIN" if train else "TEST"
      self.name = name
      self.train = train
      self.datapath = datapath
      self.scales = [2,3,4,8]

      self._set_filesystem()

      hrimages, lrimages = self._scan()

      

  def _set_filesystem(self):
    self.apath = os.path.join(self.datapath, self.name)
    self.hrdir = os.path.join(self.apath, '/HR')
    self.lrdir = os.path.join(self.apath, '/LR')

  def _scan(self):
    hrnames = sorted(glob.glob(os.path.join(self.hrdir, "*")))
    lrnames = [[] for _ in self.scales]
    for si, s in enumerate(self.scales):
      for f in hrnames:
        image,_ = os.path.splitext(os.path.basename(f))[0].split('x')
        lrnames[si].append(os.path.join(self.lrdir, '{}x{}.png'.format(image, s)))
    return hrnames, lrnames
