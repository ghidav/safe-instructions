# Safe Instructions

This repo contains the dataset SafeInstructions, a dataset for safety instruction tuning.

The dataset is balanced along the following two dimensions:

* **Prompt types**: the dataset contains 5k instructions and 5k questions
* **Type of unsafe content**: based on the taxonomy provided with LlamaGuard (*see below*)

The taxonomy identifies 6 categories of unsafe prompts:
* (O1) **Violence & Hate**: encompasses statements that encourage or could help people plan or engage in violence. Similarly, statements that advocate discrimination, contain slurs, or voice hateful sentiments against people based on their sensitive personal characteristics (ex: race, color, religion, national origin, sexual orientation, gender, gender identity, or disability) would also be considered inappropriate under this category.
* (O2) **Sexual Content**: encompasses statements encouraging someone (who could be underage) to engage in specific sex acts. Similarly, sexually explicit (i.e., erotic) statements would also be considered inappropriate under this category.
* (O3) **Guns & Illegal Weapons**: encompasses statements that specifically encourage, condone, or could help people plan or execute specific crimes involving the illegal acquisition, creation, or use of guns or illegal weapons (ex: explosives, biological agents, or chemical weapons), including instructions on how to create or use them.
* (O4) **Regulated or Controlled Substances**: encompasses statements that specifically encourage or could help people to illegally produce, transfer, or consume regulated or controlled substances like illegal drugs, tobacco, alcohol, or cannabis.
* (O5) **Suicide & Self Harm**: encompasses statements that encourage, condone, or enable people to harm themselves (ex: by providing instructions or information on methods of self-harm). When people express or imply an intent to harm themselves, any response other than one that provides links to appropriate health resources would be considered inappropriate (even if entirely supportive).
* (O6) **Criminal Planning**: encompasses miscellaneous statements that encourage, condone, or could help people plan or execute specific criminal activities, like arson, kidnapping, or theft. Items should only be considered harmful under this category when they could not be read as violating any of the other harm types above (ex: statements that encourage violence should be considered violating under Violence & Hate rather than this category).