import cx_Freeze

executables = [cx_Freeze.Executable("moving.py")]

cx_Freeze.setup(
    name="Flappy Bird",
    options={"build_exe":
        {"packages":
            ["pygame"],"include_files":["images"]}},
    executables = executables
)


