import tac
import os


def auto_correct():
    path_to_root = os.path.join(".")
    code_source = tac.SourceCode(os.path.join(path_to_root, "src"), logging_func=print)
    tests_source = tac.SourceTests(os.path.join(path_to_root, "tests"), logging_func=print)
    auto_corrector = tac.Tester(
        code_source, tests_source,
        report_dir="report_dir",
        logging_func=print,
        weights={
            tac.Tester.PEP8_KEY: 10.0,
            tac.Tester.PERCENT_PASSED_KEY: 10.0,
            tac.Tester.CODE_COVERAGE_KEY: 20.0,
            tac.Tester.MASTER_PERCENT_PASSED_KEY: 30.0,
        },
    )
    auto_corrector.run(overwrite=False, clear_pytest_temporary_files=True)
    print(auto_corrector.report)
    auto_corrector.push_report_to("auto")
    auto_corrector.rm_report_dir()


if __name__ == "__main__":
    auto_correct()
    # or run the following command in the terminal:
    # python -m tac --code-src-path="src" --tests-src-path="tests" --push_report_to="auto"
    # --code_coverage-weight=20 --percent_passed-weight=10 --PEP8-weight=10 --master_percent_passed-weight=30
    # --rm-report-dir --overwrite --debug
