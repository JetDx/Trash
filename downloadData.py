from roboflow import Roboflow
rf = Roboflow(api_key="z6kLqObeQ8IrxtiKYBSt")
project = rf.workspace("jonathan-edwards-telaumbanua").project("trash-examinator")
version = project.version(10)
dataset = version.download("yolov5")