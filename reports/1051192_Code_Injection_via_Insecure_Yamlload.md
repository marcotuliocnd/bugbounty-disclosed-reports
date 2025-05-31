# Code Injection via Insecure Yaml.load

## Report Details
- **Report ID**: 1051192
- **URL**: https://hackerone.com/reports/1051192
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-12-05T14:20:39.660Z
- **Disclosed**: 2021-05-01T18:00:28.868Z

## Reporter
- **Username**: r44mb00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Report Submission Form

## Summary:
The Kubernetes repo and tool, [test-infra](https://github.com/kubernetes/test-infra), uses the insecure yaml.load() function to set or update the `Gubernator` configuration with a yaml file which allows for code injection.
Vulnerable Line of Code:
[https://github.com/kubernetes/test-infra/blob/master/gubernator/main.py#L36](https://github.com/kubernetes/test-infra/blob/master/gubernator/main.py#L36)
[https://github.com/kubernetes/test-infra/blob/master/gubernator/update_config.py#L35](https://github.com/kubernetes/test-infra/blob/master/gubernator/update_config.py#L35)
[https://github.com/kubernetes/test-infra/blob/master/gubernator/update_config.py#L48](https://github.com/kubernetes/test-infra/blob/master/gubernator/update_config.py#L48)  
Vulnerable Files and functions: main.py:get_app_config()
                                                                         update_config.py:main()

## Kubernetes Version:
Latest version: Master branch on Github

## Component Version:
Latest version: Master branch on Github

## Steps To Reproduce:

  1. Install the `Gubernator` frontend.
  2. save the provided `config.yaml` file as the configuration file for Guberator, keep the same name.
  3. Once you update the configuration the poc should be executed and a `ls` should be executed. 

To Facilitate the process I have created a poc.py script in which I extracted the vulnerable code blocks from the test-infra repository to simulate the tools behaviour (Only from the main.py to illustrate the concept, same applies to the other occurence). 
### Steps to run the PoC:
   1. Save the `poc.py` script. 
   2. Save the `config.yaml` file in the same folder as the script. 
   3. Run the script using `python3 poc.py`. 
   4. The command `ls` should be executed. Note that any other command can be executed. 

### Important Exploit Conditions:
The extent of the exploitability of this vulnerability is limited by the version of PyYaml that the victim has installed.
For versions of PyYaml => 5.1 the only way to achieve command execution is to have `Gubernator` running embedded in a component that previously imports the subprocess module. For example Flask.
For versions of PyYaml < 5.1 the vulnerability is always exploitable and command execution can always be achieved.
Note that the former is always the case for the `test-infra/Gubernator` repo given that the requirements set `PyYAML > 5.1`. For this reason I have checked the `Attack Complexity` of the CVSS score as high. Exploitability is difficult but still possible in the worst case scenario. 

Solution:
As a possible solution I suggest changing the vulnerable and deprecated function for its secure equivalent, `safe_load()`.

## Supporting Material/References:
Details on the vulnerability and how to exploit in general can be found in this great [article](https://www.exploit-db.com/docs/english/47655-yaml-deserialization-attack-in-python.pdf)
  * `poc.py`: Python3 script with the proof of concept. 
  * `config.yaml`: Payload file for the PoC.
  * `evidence.png`: Screenshot of the script ran on my local machine.

## Impact

An attacker can exploit this vulnerability by crafting a malicious YAML file in order to execute system commands. An attacker can either find a way to load a malicious configuration file or entice a victim into loading it. This results in Command Execution.
For this reason I have marked the `User Interaction` of the CVSS score as required.

## Attachments
- evidence.png
- config.yaml
- poc.py
