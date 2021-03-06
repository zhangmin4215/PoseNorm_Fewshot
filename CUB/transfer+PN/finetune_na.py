import sys
import torch
import numpy as np
import torch.nn as nn
from functools import partial
sys.path.append('../../')
from utils import transfer_train,transfer_eval,networks,dataloader,util

args,name = util.train_parser()

pm = util.Path_Manager_NA('../../dataset/na_fewshot',args=args)

config = util.Config(args=args,
                     name=name,
                     suffix='na')

train_loader = dataloader.normal_train_dataloader(data_path=pm.test_refer,
                                                  batch_size=args.batch_size)
num_class = len(train_loader.dataset.classes)

model = networks.Transfer_PN(num_part=args.num_part,
                             resnet=args.resnet)
model.cuda()
model.load_state_dict(torch.load(args.load_path))
model.linear_classifier = nn.Linear(model.dim,num_class).cuda()

train_func = partial(transfer_train.default_train,train_loader=train_loader)

tm = util.TM_transfer_PN_finetune(args,pm,config,
                               train_func=train_func)

tm.train(model)

transfer_eval.eval_test(model,pm,config)