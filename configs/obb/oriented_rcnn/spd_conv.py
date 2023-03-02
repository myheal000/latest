_base_ = './faster_rcnn_orpn_r50_fpn_3x_hrsc.py'
model = dict(pretrained=None, backbone=dict(type='ResNet_spd',block = 'BottleNeck',num_block =[3, 4, 6, 3]))