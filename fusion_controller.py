# fusion_controller.py

import adsk.core, adsk.fusion, traceback, sys

# コマンドライン引数の取得
command = sys.argv[1] if len(sys.argv) > 1 else ""

def create_cube(size):
    app = adsk.core.Application.get()
    ui = app.userInterface
    design = app.activeProduct
    root = design.rootComponent
    sketches = root.sketches
    xyPlane = root.xYConstructionPlane

    # スケッチ作成
    sketch = sketches.add(xyPlane)
    sketch.sketchCurves.sketchLines.addTwoPointRectangle(
        adsk.core.Point3D.create(0, 0, 0),
        adsk.core.Point3D.create(size, size, 0)
    )

    # 押し出し
    prof = sketch.profiles.item(0)
    extrudes = root.features.extrudeFeatures
    extInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
    distance = adsk.core.ValueInput.createByReal(size)
    extInput.setDistanceExtent(False, distance)
    extrudes.add(extInput)
    print(f"Created cube of size {size} mm")

try:
    if command.startswith("create_cube"):
        _, val = command.split()
        create_cube(float(val))
    else:
        print("Unknown command")
except Exception as e:
    print("Fusion script error:", traceback.format_exc())
