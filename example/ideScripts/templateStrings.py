"""
Template scripts for generating workspace files:
    - c_cpp_properties.json
    - tasks.json
    - makefile strings/functions
    - buildData.json
"""

launchName_Debug = "Cortex debug"
launchName_Python = "Debug current Python file"

taskName_build = "Build project"
taskName_compile = "Compile current file"
taskName_clean = "Delete build folder"

taskName_CPU_buildDownloadRun = "CPU: Build, Download and run"
taskName_CPU_downloadRun = "CPU: Download and run"
taskName_CPU_resetRun = "CPU: Reset and run"
taskName_CPU_halt = "CPU: Halt"
taskName_CPU_run = "CPU: Run"

taskName_Python = "Run Python file"
taskName_OpenCubeMX = "Open CubeMX project"
taskName_updateWorkspace = "Update workspace"

#########################################################################################################
c_cpp_template = """{
    "env" : {
        "____________________USER_FIELDS_CAN_BE_MODIFIED____________________": "",
        "user_cSources": [],
        "user_asmSources": [],
        "user_cIncludes": [],
        "user_asmIncludes": [],
        "user_cDefines": ["AVOID_EMPTY_DEFINE_FIELD_C"],
        "user_asmDefines": ["AVOID_EMPTY_DEFINE_FIELD_ASM"],
        "user_cFlags" : [],
        "user_asmFlags" : [],

        "____________________DO_NOT_MODIFY_FIELDS_BELOW____________________": "",
        "cubemx_sourceFiles": [],
        "cubemx_includes": [],
        "cubemx_defines": [],
        "gccExePath": "",
        "gccIncludePath": ""
    },
    "configurations": [
        {
            "name": "devTestBoard name of the project?",
            "intelliSenseMode": "msvc-x64",
            "includePath": [
                "${workspaceFolder}",
                "${cubemx_includes}",
                "${gccIncludePath}",
                "${user_cIncludes}",
                "${user_asmIncludes}"
            ],
            "browse": {
                "path": [
                    "${workspaceFolder}",
                    "${cubemx_includes}",
                    "${gccIncludePath}",
                    "${user_cIncludes}",
                    "${user_asmIncludes}"
                ],
                "limitSymbolsToIncludedHeaders": true
            },
            "defines": [
                "${cubemx_defines}",
                "${user_cDefines}",
                "${user_asmDefines}"
            ],
            "forcedInclude": [
            ],
            "compilerPath": "${gccExePath}",
            "cStandard": "c11",
            "cppStandard": "c++17"
        }
    ],
    "version": 4
}
"""
#########################################################################################################
versionString = "Version ***"
lastRunString = "Last run: ***"

#########################################################################################################
makefileHeader = ('#' * 100) + "\n"
makefileHeader += "# Makefile generated by updateMakefile.py\n"
makefileHeader += "# " + versionString + " \n"
makefileHeader += "# " + lastRunString + " \n"
makefileHeader += ('#' * 100) + "\n"

#########################################################################################################
printMakefileVariableFunction = "print-%:"
printMakefileDefaultString = "VARIABLE="
printMakefileVariable = "#######################################\n"
printMakefileVariable += "# Print makefile variables\n"
printMakefileVariable += "#######################################\n"
printMakefileVariable += printMakefileVariableFunction + "\n"
printMakefileVariable += "\t@echo " + printMakefileDefaultString + "$($*)\n"

#########################################################################################################
cleanFunctionNameSearchString = "clean:"
cleanBuildDirFunctionName = "clean-build-dir"
cleanBuildDirFunction = "#######################################\n"
cleanBuildDirFunction += "# Clean build directory content \n"
cleanBuildDirFunction += "#######################################\n"
cleanBuildDirFunction += cleanBuildDirFunctionName + ":\n"
cleanBuildDirFunction += "\t@echo Build folder: '$(BUILD_DIR)' clean request (files with spaces and folders will not be removed):\n"
cleanBuildDirFunction += "\t@$(foreach file, $(wildcard $(BUILD_DIR)/*), rm -f $(file))\n"
cleanBuildDirFunction += "\t@echo OK.\n"

#########################################################################################################
taskTemplate = """{
            "label": "Update workspace",
            "type": "shell",
            "command": "python",
            "args": [
                "${workspaceFolder}\\\\test.py"
            ],
            "group": "none",
            "presentation": {
                "reveal": "always",
                "panel": "shared"
            },
            "problemMatcher": {
            }
        }
"""

tasksFileTemplate = """{
    "version": "2.0.0",
    "tasks": ["""
tasksFileTemplate += """
    ]
}
"""

#########################################################################################################
buildDataTemplate = """{
    "ABOUT1": "This file holds combined user and CubeMX generated Makefile workspace dependecies.",
    "ABOUT2": "User should not edit this fields, instead it should edit 'c_cpp_properties.json'",
    "ABOUT3": "This file is regenerated on 'Update workspace' task.",
    "VERSION": "",
    "LAST_RUN": "",
    "cSources": [],
    "asmSources": [],
    "cIncludes": [],
    "asmIncludes": [],
    "cDefines": [],
    "asmDefines": [],
    "cFlags" : [],
    "asmFlags" : [],
    "buildDir": "",
    "gccInludePath": "",
    "gccExePath": "",
    "buildToolsPath": "",
    "openOCDPath": "",
    "openOCDInterfacePath":"",
    "openOCDTargetPath": ""
}
"""

#########################################################################################################
launchFileTemplate = """{
    "version": "0.2.0",
    "configurations": [
    ]
}
"""
