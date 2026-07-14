# OWASP ASVS 4.0.3 — throughline source

This document is **generated from the graph** by `tl docs`; `tl docs --check` gates
it in CI. The prose headings are hand-owned — everything between `tl:*` markers is
injected from the YAML items, so the published spec can never drift from the graph.

This source is a faithful, complete cut of **OWASP ASVS v4.0.3**: every chapter is a
`user_requirement`, and every non-retired verification requirement is a
`system_requirement` that `implements` its chapter. The published ASVS number lives in
`attrs.source_ref` (e.g. `V2.1.1`); the ASVS level in `attrs.level`. The throughline
UIDs are this source's own and immutable — a consumer cites a clause as `asvs:SR-0003`,
never by its ASVS number.

It carries
<!-- tl:count type == 'user_requirement' -->
14
<!-- tl:end --> chapters and
<!-- tl:count type == 'system_requirement' -->
278
<!-- tl:end --> verification requirements. (ASVS clauses retired as
`[DELETED]` in 4.0.3 carry no level and are intentionally omitted.)

## Purpose

<!-- tl:item INT-0001 -->
**INT-0001 — An application's security is verifiable against a graded, testable baseline** — `intent`, status `approved`

> The OWASP Application Security Verification Standard exists so that an application's security controls can be verified against a normative, level-graded set of requirements — giving developers, testers and procurers a shared baseline rather than ad-hoc judgement.

**source_ref**: ASVS 4.0.3
<!-- tl:end -->

## V1 Architecture, Design and Threat Modeling

<!-- tl:item UR-0001 -->
**UR-0001 — V1 Architecture, Design and Threat Modeling** — `user_requirement`, status `approved`

> Security controls are designed in, not bolted on — the application has a secure development lifecycle, threat modeling, and a documented, verifiable security architecture.

**source_ref**: V1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V1.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0001 | system_requirement | approved | Secure software development lifecycle |
| SR-0002 | system_requirement | approved | Threat modeling for design changes |
| SR-0007 | system_requirement | approved | All user stories and features contain functional security constraints |
| SR-0008 | system_requirement | approved | Documentation and justification of all the application's trust boundaries |
| SR-0009 | system_requirement | approved | Definition and security analysis of the application's high-level architecture and all connected |
| SR-0010 | system_requirement | approved | Implementation of centralized |
| SR-0011 | system_requirement | approved | Availability of a secure coding checklist |
| SR-0012 | system_requirement | approved | The use of unique or special low-privilege operating system accounts for all application components |
| SR-0013 | system_requirement | approved | Communications between application components |
| SR-0014 | system_requirement | approved | The application uses a single vetted authentication mechanism that is known to be secure |
| SR-0015 | system_requirement | approved | All authentication pathways and identity management APIs implement consistent authentication |
| SR-0016 | system_requirement | approved | Trusted enforcement points |
| SR-0017 | system_requirement | approved | The application uses a single and well-vetted access control mechanism for accessing protected data |
| SR-0018 | system_requirement | approved | Attribute or feature-based access control is used whereby the code checks the user's authorization |
| SR-0019 | system_requirement | approved | Input and output requirements clearly define how to handle and process data based on type |
| SR-0020 | system_requirement | approved | Serialization is not used when communicating with untrusted clients |
| SR-0021 | system_requirement | approved | Input validation is enforced on a trusted service layer |
| SR-0022 | system_requirement | approved | Output encoding occurs close to or by the interpreter for which it is intended |
| SR-0023 | system_requirement | approved | There is an explicit policy for management of cryptographic keys and that a cryptographic key |
| SR-0024 | system_requirement | approved | Consumers of cryptographic services protect key material and other secrets by using key vaults or |
| SR-0025 | system_requirement | approved | All keys and passwords are replaceable and are part of a well-defined process to re-encrypt |
| SR-0026 | system_requirement | approved | The architecture treats client-side secrets--such as symmetric keys |
| SR-0027 | system_requirement | approved | A common logging format and approach is used across the system |
| SR-0028 | system_requirement | approved | Logs are securely transmitted to a preferably remote system for analysis |
| SR-0029 | system_requirement | approved | All sensitive data is identified and classified into protection levels |
| SR-0030 | system_requirement | approved | All protection levels have an associated set of protection requirements |
| SR-0031 | system_requirement | approved | The application encrypts communications between components |
| SR-0032 | system_requirement | approved | Application components verify the authenticity of each side in a communication link to prevent |
| SR-0033 | system_requirement | approved | A source code control system is in use |
| SR-0034 | system_requirement | approved | The definition and documentation of all application components in terms of the business or security |
| SR-0035 | system_requirement | approved | All high-value business logic flows |
| SR-0036 | system_requirement | approved | All high-value business logic flows |
| SR-0037 | system_requirement | approved | User-uploaded files - if required to be displayed or downloaded from the application - are served |
| SR-0038 | system_requirement | approved | The segregation of components of differing trust levels through well-defined security controls |
| SR-0039 | system_requirement | approved | Binary signatures |
| SR-0040 | system_requirement | approved | The build pipeline warns of out-of-date or insecure components and takes appropriate actions |
| SR-0041 | system_requirement | approved | The build pipeline contains a build step to automatically build and verify the secure deployment of |
| SR-0042 | system_requirement | approved | Application deployments adequately sandbox |
| SR-0043 | system_requirement | approved | The application does not use unsupported |
<!-- tl:end -->

## V2 Authentication

<!-- tl:item UR-0002 -->
**UR-0002 — V2 Authentication** — `user_requirement`, status `approved`

> The application verifies the identity of users securely — password strength, storage, recovery and general authenticator controls are all held to a graded baseline.

**source_ref**: V2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V2.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0003 | system_requirement | approved | Minimum password length |
| SR-0004 | system_requirement | approved | Long passwords permitted |
| SR-0005 | system_requirement | approved | No password truncation |
| SR-0006 | system_requirement | approved | Passwords checked against breached sets |
| SR-0044 | system_requirement | approved | Any printable Unicode character |
| SR-0045 | system_requirement | approved | Users can change their password |
| SR-0046 | system_requirement | approved | Password change functionality requires the user's current and new password |
| SR-0047 | system_requirement | approved | A password strength meter is provided to help users set a stronger password |
| SR-0048 | system_requirement | approved | There are no password composition rules limiting the type of characters permitted |
| SR-0049 | system_requirement | approved | There are no periodic credential rotation or password history requirements |
| SR-0050 | system_requirement | approved | "paste" functionality |
| SR-0051 | system_requirement | approved | The user can choose to either temporarily view the entire masked password |
| SR-0052 | system_requirement | approved | Anti-automation controls are effective at mitigating breached credential testing |
| SR-0053 | system_requirement | approved | The use of weak authenticators (such as SMS and email) is limited to secondary verification and |
| SR-0054 | system_requirement | approved | Secure notifications are sent to users after updates to authentication details |
| SR-0055 | system_requirement | approved | Impersonation resistance against phishing |
| SR-0056 | system_requirement | approved | Where a Credential Service Provider (CSP) and the application verifying authentication are separated |
| SR-0057 | system_requirement | approved | Replay resistance through the mandated use of One-time Passwords (OTP) devices |
| SR-0058 | system_requirement | approved | Intent to authenticate by requiring the entry of an OTP token or user-initiated action such as a |
| SR-0059 | system_requirement | approved | System generated initial passwords or activation codes SHOULD be securely randomly generated |
| SR-0060 | system_requirement | approved | Enrollment and use of user-provided authentication devices are supported |
| SR-0061 | system_requirement | approved | Renewal instructions are sent with sufficient time to renew time bound authenticators |
| SR-0062 | system_requirement | approved | Passwords are stored in a form that is resistant to offline attacks |
| SR-0063 | system_requirement | approved | The salt is at least 32 bits in length and be chosen arbitrarily to minimize salt value collisions |
| SR-0064 | system_requirement | approved | If PBKDF2 is used |
| SR-0065 | system_requirement | approved | If bcrypt is used |
| SR-0066 | system_requirement | approved | An additional iteration of a key derivation function is performed |
| SR-0067 | system_requirement | approved | A system generated initial activation or recovery secret is not sent in clear text to the user |
| SR-0068 | system_requirement | approved | Password hints or knowledge-based authentication (so-called "secret questions") are not present |
| SR-0069 | system_requirement | approved | Password credential recovery does not reveal the current password in any way |
| SR-0070 | system_requirement | approved | Shared or default accounts are not present (e |
| SR-0071 | system_requirement | approved | If an authentication factor is changed or replaced |
| SR-0072 | system_requirement | approved | Forgotten password |
| SR-0073 | system_requirement | approved | If OTP or multi-factor authentication factors are lost |
| SR-0074 | system_requirement | approved | Lookup secrets can be used only once |
| SR-0075 | system_requirement | approved | Lookup secrets have sufficient randomness (112 bits of entropy) |
| SR-0076 | system_requirement | approved | Lookup secrets are resistant to offline attacks |
| SR-0077 | system_requirement | approved | Clear text out of band (NIST "restricted") authenticators |
| SR-0078 | system_requirement | approved | The out of band verifier expires out of band authentication requests |
| SR-0079 | system_requirement | approved | The out of band verifier authentication requests |
| SR-0080 | system_requirement | approved | The out of band authenticator and verifier communicates over a secure independent channel |
| SR-0081 | system_requirement | approved | The out of band verifier retains only a hashed version of the authentication code |
| SR-0082 | system_requirement | approved | The initial authentication code is generated by a secure random number generator |
| SR-0083 | system_requirement | approved | Time-based OTPs have a defined lifetime before expiring |
| SR-0084 | system_requirement | approved | Symmetric keys used to verify submitted OTPs are highly protected |
| SR-0085 | system_requirement | approved | Approved cryptographic algorithms are used in the generation |
| SR-0086 | system_requirement | approved | Time-based OTP can be used only once within the validity period |
| SR-0087 | system_requirement | approved | If a time-based multi-factor OTP token is re-used during the validity period |
| SR-0088 | system_requirement | approved | Physical single-factor OTP generator can be revoked in case of theft or other loss |
| SR-0089 | system_requirement | approved | Biometric authenticators are limited to use only as secondary factors in conjunction with either |
| SR-0090 | system_requirement | approved | Cryptographic keys used in verification are stored securely and protected against disclosure |
| SR-0091 | system_requirement | approved | The challenge nonce is at least 64 bits in length |
| SR-0092 | system_requirement | approved | Approved cryptographic algorithms are used in the generation |
| SR-0093 | system_requirement | approved | Intra-service secrets do not rely on unchanging credentials such as passwords |
| SR-0094 | system_requirement | approved | If passwords are required for service authentication |
| SR-0095 | system_requirement | approved | Passwords are stored with sufficient protection to prevent offline recovery attacks |
| SR-0096 | system_requirement | approved | Passwords |
<!-- tl:end -->

## V3 Session Management

<!-- tl:item UR-0003 -->
**UR-0003 — V3 Session Management** — `user_requirement`, status `approved`

> Verification requirements for Session Management (V3).

**source_ref**: V3
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V3.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0097 | system_requirement | approved | The application never reveals session tokens in URL parameters |
| SR-0098 | system_requirement | approved | The application generates a new session token on user authentication |
| SR-0099 | system_requirement | approved | Session tokens possess at least 64 bits of entropy |
| SR-0100 | system_requirement | approved | The application only stores session tokens in the browser using secure methods such as |
| SR-0101 | system_requirement | approved | Session tokens are generated using approved cryptographic algorithms |
| SR-0102 | system_requirement | approved | Logout and expiration invalidate the session token |
| SR-0103 | system_requirement | approved | If authenticators permit users to remain logged in |
| SR-0104 | system_requirement | approved | The application gives the option to terminate all other active sessions after a successful password |
| SR-0105 | system_requirement | approved | Users are able to view and (having re-entered login credentials) log out of any or all currently |
| SR-0106 | system_requirement | approved | Cookie-based session tokens have the 'Secure' attribute set |
| SR-0107 | system_requirement | approved | Cookie-based session tokens have the 'HttpOnly' attribute set |
| SR-0108 | system_requirement | approved | Cookie-based session tokens utilize the 'SameSite' attribute to limit exposure to cross-site |
| SR-0109 | system_requirement | approved | Cookie-based session tokens use the "__Host-" prefix so cookies are only sent to the host that |
| SR-0110 | system_requirement | approved | If the application is published under a domain name with other applications that set or use session |
| SR-0111 | system_requirement | approved | The application allows users to revoke OAuth tokens that form trust relationships with linked |
| SR-0112 | system_requirement | approved | The application uses session tokens rather than static API secrets and keys |
| SR-0113 | system_requirement | approved | Stateless session tokens use digital signatures |
| SR-0114 | system_requirement | approved | Relying Parties (RPs) specify the maximum authentication time to Credential Service Providers |
| SR-0115 | system_requirement | approved | Credential Service Providers (CSPs) inform Relying Parties (RPs) of the last authentication event |
| SR-0116 | system_requirement | approved | The application ensures a full |
<!-- tl:end -->

## V4 Access Control

<!-- tl:item UR-0004 -->
**UR-0004 — V4 Access Control** — `user_requirement`, status `approved`

> Verification requirements for Access Control (V4).

**source_ref**: V4
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V4.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0117 | system_requirement | approved | The application enforces access control rules on a trusted service layer |
| SR-0118 | system_requirement | approved | All user and data attributes and policy information used by access controls cannot be manipulated |
| SR-0119 | system_requirement | approved | The principle of least privilege exists - users should only be able to access functions |
| SR-0120 | system_requirement | approved | Access controls fail securely including when an exception occurs |
| SR-0121 | system_requirement | approved | Sensitive data and APIs are protected against Insecure Direct Object Reference (IDOR) attacks |
| SR-0122 | system_requirement | approved | The application or framework enforces a strong anti-CSRF mechanism to protect authenticated |
| SR-0123 | system_requirement | approved | Administrative interfaces use appropriate multi-factor authentication to prevent unauthorized use |
| SR-0124 | system_requirement | approved | Directory browsing is disabled unless deliberately desired |
| SR-0125 | system_requirement | approved | The application has additional authorization (such as step up or adaptive authentication) for lower |
<!-- tl:end -->

## V5 Validation, Sanitization and Encoding

<!-- tl:item UR-0005 -->
**UR-0005 — V5 Validation, Sanitization and Encoding** — `user_requirement`, status `approved`

> Verification requirements for Validation, Sanitization and Encoding (V5).

**source_ref**: V5
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V5.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0126 | system_requirement | approved | The application has defenses against HTTP parameter pollution attacks |
| SR-0127 | system_requirement | approved | Frameworks protect against mass parameter assignment attacks |
| SR-0128 | system_requirement | approved | All input (HTML form fields |
| SR-0129 | system_requirement | approved | Structured data is strongly typed and validated against a defined schema including allowed |
| SR-0130 | system_requirement | approved | URL redirects and forwards only allow destinations which appear on an allow list |
| SR-0131 | system_requirement | approved | All untrusted HTML input from WYSIWYG editors or similar is properly sanitized with an HTML |
| SR-0132 | system_requirement | approved | Unstructured data is sanitized to enforce safety measures such as allowed characters and length |
| SR-0133 | system_requirement | approved | The application sanitizes user input before passing to mail systems to protect against SMTP or IMAP |
| SR-0134 | system_requirement | approved | The application avoids the use of eval() or other dynamic code execution features |
| SR-0135 | system_requirement | approved | The application protects against template injection attacks by ensuring that any user input being |
| SR-0136 | system_requirement | approved | The application protects against SSRF attacks |
| SR-0137 | system_requirement | approved | The application sanitizes |
| SR-0138 | system_requirement | approved | The application sanitizes |
| SR-0139 | system_requirement | approved | Output encoding is relevant for the interpreter and context required |
| SR-0140 | system_requirement | approved | Output encoding preserves the user's chosen character set and locale |
| SR-0141 | system_requirement | approved | Context-aware |
| SR-0142 | system_requirement | approved | Data selection or database queries (e |
| SR-0143 | system_requirement | approved | Where parameterized or safer mechanisms are not present |
| SR-0144 | system_requirement | approved | The application protects against JSON injection attacks |
| SR-0145 | system_requirement | approved | The application protects against LDAP injection vulnerabilities |
| SR-0146 | system_requirement | approved | The application protects against OS command injection and that operating system calls use |
| SR-0147 | system_requirement | approved | The application protects against Local File Inclusion (LFI) or Remote File Inclusion (RFI) attacks |
| SR-0148 | system_requirement | approved | The application protects against XPath injection or XML injection attacks |
| SR-0149 | system_requirement | approved | The application uses memory-safe string |
| SR-0150 | system_requirement | approved | Format strings do not take potentially hostile input |
| SR-0151 | system_requirement | approved | Sign |
| SR-0152 | system_requirement | approved | Serialized objects use integrity checks or are encrypted to prevent hostile object creation or data |
| SR-0153 | system_requirement | approved | The application correctly restricts XML parsers to only use the most restrictive configuration |
| SR-0154 | system_requirement | approved | Deserialization of untrusted data is avoided or is protected in both custom code and third-party |
| SR-0155 | system_requirement | approved | When parsing JSON in browsers or JavaScript-based backends |
<!-- tl:end -->

## V6 Stored Cryptography

<!-- tl:item UR-0006 -->
**UR-0006 — V6 Stored Cryptography** — `user_requirement`, status `approved`

> Verification requirements for Stored Cryptography (V6).

**source_ref**: V6
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V6.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0156 | system_requirement | approved | Regulated private data is stored encrypted while at rest |
| SR-0157 | system_requirement | approved | Regulated health data is stored encrypted while at rest |
| SR-0158 | system_requirement | approved | Regulated financial data is stored encrypted while at rest |
| SR-0159 | system_requirement | approved | All cryptographic modules fail securely |
| SR-0160 | system_requirement | approved | Industry proven or government approved cryptographic algorithms |
| SR-0161 | system_requirement | approved | Encryption initialization vector |
| SR-0162 | system_requirement | approved | Random number |
| SR-0163 | system_requirement | approved | Known insecure block modes (i |
| SR-0164 | system_requirement | approved | Nonces |
| SR-0165 | system_requirement | approved | Encrypted data is authenticated via signatures |
| SR-0166 | system_requirement | approved | All cryptographic operations are constant-time |
| SR-0167 | system_requirement | approved | All random numbers |
| SR-0168 | system_requirement | approved | Random GUIDs are created using the GUID v4 algorithm |
| SR-0169 | system_requirement | approved | Random numbers are created with proper entropy even when the application is under heavy load |
| SR-0170 | system_requirement | approved | A secrets management solution such as a key vault is used to securely create |
| SR-0171 | system_requirement | approved | Key material is not exposed to the application but instead uses an isolated security module like a |
<!-- tl:end -->

## V7 Error Handling and Logging

<!-- tl:item UR-0007 -->
**UR-0007 — V7 Error Handling and Logging** — `user_requirement`, status `approved`

> Verification requirements for Error Handling and Logging (V7).

**source_ref**: V7
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V7.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0172 | system_requirement | approved | The application does not log credentials or payment details |
| SR-0173 | system_requirement | approved | The application does not log other sensitive data as defined under local privacy laws or relevant |
| SR-0174 | system_requirement | approved | The application logs security relevant events including successful and failed authentication events |
| SR-0175 | system_requirement | approved | Each log event includes necessary information that would allow for a detailed investigation of the |
| SR-0176 | system_requirement | approved | All authentication decisions are logged |
| SR-0177 | system_requirement | approved | All access control decisions can be logged and all failed decisions are logged |
| SR-0178 | system_requirement | approved | All logging components appropriately encode data to prevent log injection |
| SR-0179 | system_requirement | approved | Security logs are protected from unauthorized access and modification |
| SR-0180 | system_requirement | approved | Time sources are synchronized to the correct time and time zone |
| SR-0181 | system_requirement | approved | A generic message is shown when an unexpected or security sensitive error occurs |
| SR-0182 | system_requirement | approved | Exception handling (or a functional equivalent) is used across the codebase to account for expected |
| SR-0183 | system_requirement | approved | A "last resort" error handler is defined which will catch all unhandled exceptions |
<!-- tl:end -->

## V8 Data Protection

<!-- tl:item UR-0008 -->
**UR-0008 — V8 Data Protection** — `user_requirement`, status `approved`

> Verification requirements for Data Protection (V8).

**source_ref**: V8
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V8.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0184 | system_requirement | approved | The application protects sensitive data from being cached in server components such as load |
| SR-0185 | system_requirement | approved | All cached or temporary copies of sensitive data stored on the server are protected from |
| SR-0186 | system_requirement | approved | The application minimizes the number of parameters in a request |
| SR-0187 | system_requirement | approved | The application can detect and alert on abnormal numbers of requests |
| SR-0188 | system_requirement | approved | Regular backups of important data are performed and that test restoration of data is performed |
| SR-0189 | system_requirement | approved | Backups are stored securely to prevent data from being stolen or corrupted |
| SR-0190 | system_requirement | approved | The application sets sufficient anti-caching headers so that sensitive data is not cached in modern |
| SR-0191 | system_requirement | approved | Data stored in browser storage (such as localStorage |
| SR-0192 | system_requirement | approved | Authenticated data is cleared from client storage |
| SR-0193 | system_requirement | approved | Sensitive data is sent to the server in the HTTP message body or headers |
| SR-0194 | system_requirement | approved | Users have a method to remove or export their data on demand |
| SR-0195 | system_requirement | approved | Users are provided clear language regarding collection and use of supplied personal information and |
| SR-0196 | system_requirement | approved | All sensitive data created and processed by the application has been identified |
| SR-0197 | system_requirement | approved | Accessing sensitive data is audited (without logging the sensitive data itself) |
| SR-0198 | system_requirement | approved | Sensitive information contained in memory is overwritten as soon as it is no longer required to |
| SR-0199 | system_requirement | approved | Sensitive or private information that is required to be encrypted |
| SR-0200 | system_requirement | approved | Sensitive personal information is subject to data retention classification |
<!-- tl:end -->

## V9 Communication

<!-- tl:item UR-0009 -->
**UR-0009 — V9 Communication** — `user_requirement`, status `approved`

> Verification requirements for Communication (V9).

**source_ref**: V9
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V9.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0201 | system_requirement | approved | TLS is used for all client connectivity |
| SR-0202 | system_requirement | approved | Using up to date TLS testing tools that only strong cipher suites are enabled |
| SR-0203 | system_requirement | approved | Only the latest recommended versions of the TLS protocol are enabled |
| SR-0204 | system_requirement | approved | Connections to and from the server use trusted TLS certificates |
| SR-0205 | system_requirement | approved | Encrypted communications such as TLS is used for all inbound and outbound connections |
| SR-0206 | system_requirement | approved | All encrypted connections to external systems that involve sensitive information or functions are |
| SR-0207 | system_requirement | approved | Proper certification revocation |
| SR-0208 | system_requirement | approved | Backend TLS connection failures are logged |
<!-- tl:end -->

## V10 Malicious Code

<!-- tl:item UR-0010 -->
**UR-0010 — V10 Malicious Code** — `user_requirement`, status `approved`

> Verification requirements for Malicious Code (V10).

**source_ref**: V10
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V10.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0209 | system_requirement | approved | A code analysis tool is in use that can detect potentially malicious code |
| SR-0210 | system_requirement | approved | The application source code and third party libraries do not contain unauthorized phone home or |
| SR-0211 | system_requirement | approved | The application does not ask for unnecessary or excessive permissions to privacy related features |
| SR-0212 | system_requirement | approved | The application source code and third party libraries do not contain back doors |
| SR-0213 | system_requirement | approved | The application source code and third party libraries do not contain time bombs by searching for |
| SR-0214 | system_requirement | approved | The application source code and third party libraries do not contain malicious code |
| SR-0215 | system_requirement | approved | The application source code and third party libraries do not contain Easter eggs or any other |
| SR-0216 | system_requirement | approved | If the application has a client or server auto-update feature |
| SR-0217 | system_requirement | approved | The application employs integrity protections |
| SR-0218 | system_requirement | approved | The application has protection from subdomain takeovers if the application relies upon DNS entries |
<!-- tl:end -->

## V11 Business Logic

<!-- tl:item UR-0011 -->
**UR-0011 — V11 Business Logic** — `user_requirement`, status `approved`

> Verification requirements for Business Logic (V11).

**source_ref**: V11
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V11.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0219 | system_requirement | approved | The application will only process business logic flows for the same user in sequential step order |
| SR-0220 | system_requirement | approved | The application will only process business logic flows with all steps being processed in realistic |
| SR-0221 | system_requirement | approved | The application has appropriate limits for specific business actions or transactions which are |
| SR-0222 | system_requirement | approved | The application has anti-automation controls to protect against excessive calls such as mass data |
| SR-0223 | system_requirement | approved | The application has business logic limits or validation to protect against likely business risks or |
| SR-0224 | system_requirement | approved | The application does not suffer from "Time Of Check to Time Of Use" (TOCTOU) issues or other race |
| SR-0225 | system_requirement | approved | The application monitors for unusual events or activity from a business logic perspective |
| SR-0226 | system_requirement | approved | The application has configurable alerting when automated attacks or unusual activity is detected |
<!-- tl:end -->

## V12 Files and Resources

<!-- tl:item UR-0012 -->
**UR-0012 — V12 Files and Resources** — `user_requirement`, status `approved`

> Verification requirements for Files and Resources (V12).

**source_ref**: V12
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V12.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0227 | system_requirement | approved | The application will not accept large files that could fill up storage or cause a denial of service |
| SR-0228 | system_requirement | approved | The application checks compressed files (e |
| SR-0229 | system_requirement | approved | A file size quota and maximum number of files per user is enforced to ensure that a single user |
| SR-0230 | system_requirement | approved | Files obtained from untrusted sources are validated to be of expected type based on the file's |
| SR-0231 | system_requirement | approved | User-submitted filename metadata is not used directly by system or framework filesystems and that a |
| SR-0232 | system_requirement | approved | User-submitted filename metadata is validated or ignored to prevent the disclosure |
| SR-0233 | system_requirement | approved | User-submitted filename metadata is validated or ignored to prevent the disclosure or execution of |
| SR-0234 | system_requirement | approved | The application protects against Reflective File Download (RFD) by validating or ignoring |
| SR-0235 | system_requirement | approved | Untrusted file metadata is not used directly with system API or libraries |
| SR-0236 | system_requirement | approved | The application does not include and execute functionality from untrusted sources |
| SR-0237 | system_requirement | approved | Files obtained from untrusted sources are stored outside the web root |
| SR-0238 | system_requirement | approved | Files obtained from untrusted sources are scanned by antivirus scanners to prevent upload and |
| SR-0239 | system_requirement | approved | The web tier is configured to serve only files with specific file extensions to prevent |
| SR-0240 | system_requirement | approved | Direct requests to uploaded files will never be executed as HTML/JavaScript content |
| SR-0241 | system_requirement | approved | The web or application server is configured with an allow list of resources or systems to which the |
<!-- tl:end -->

## V13 API and Web Service

<!-- tl:item UR-0013 -->
**UR-0013 — V13 API and Web Service** — `user_requirement`, status `approved`

> Verification requirements for API and Web Service (V13).

**source_ref**: V13
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V13.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0242 | system_requirement | approved | All application components use the same encodings and parsers to avoid parsing attacks that exploit |
| SR-0243 | system_requirement | approved | API URLs do not expose sensitive information |
| SR-0244 | system_requirement | approved | Authorization decisions are made at both the URI |
| SR-0245 | system_requirement | approved | Requests containing unexpected or missing content types are rejected with appropriate headers (HTTP |
| SR-0246 | system_requirement | approved | Enabled RESTful HTTP methods are a valid choice for the user or action |
| SR-0247 | system_requirement | approved | JSON schema validation is in place and verified before accepting input |
| SR-0248 | system_requirement | approved | RESTful web services that utilize cookies are protected from Cross-Site Request Forgery via the use |
| SR-0249 | system_requirement | approved | REST services explicitly check the incoming Content-Type to be the expected one |
| SR-0250 | system_requirement | approved | The message headers and payload are trustworthy and not modified in transit |
| SR-0251 | system_requirement | approved | XSD schema validation takes place to ensure a properly formed XML document |
| SR-0252 | system_requirement | approved | The message payload is signed using WS-Security to ensure reliable transport between client and |
| SR-0253 | system_requirement | approved | A query allow list or a combination of depth limiting and amount limiting is used to prevent |
| SR-0254 | system_requirement | approved | GraphQL or other data layer authorization logic should be implemented at the business logic layer |
<!-- tl:end -->

## V14 Configuration

<!-- tl:item UR-0014 -->
**UR-0014 — V14 Configuration** — `user_requirement`, status `approved`

> Verification requirements for Configuration (V14).

**source_ref**: V14
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V14.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0255 | system_requirement | approved | The application build and deployment processes are performed in a secure and repeatable way |
| SR-0256 | system_requirement | approved | Compiler flags are configured to enable all available buffer overflow protections and warnings |
| SR-0257 | system_requirement | approved | Server configuration is hardened as per the recommendations of the application server and |
| SR-0258 | system_requirement | approved | The application |
| SR-0259 | system_requirement | approved | Authorized administrators can verify the integrity of all security-relevant configurations to |
| SR-0260 | system_requirement | approved | All components are up to date |
| SR-0261 | system_requirement | approved | All unneeded features |
| SR-0262 | system_requirement | approved | If application assets |
| SR-0263 | system_requirement | approved | Third party components come from pre-defined |
| SR-0264 | system_requirement | approved | A Software Bill of Materials (SBOM) is maintained of all third party libraries in use |
| SR-0265 | system_requirement | approved | The attack surface is reduced by sandboxing or encapsulating third party libraries to expose only |
| SR-0266 | system_requirement | approved | Web or application server and application framework debug modes are disabled in production to |
| SR-0267 | system_requirement | approved | The HTTP headers or any part of the HTTP response do not expose detailed version information of |
| SR-0268 | system_requirement | approved | Every HTTP response contains a Content-Type header |
| SR-0269 | system_requirement | approved | All API responses contain a Content-Disposition: attachment |
| SR-0270 | system_requirement | approved | A Content Security Policy (CSP) response header is in place that helps mitigate impact for XSS |
| SR-0271 | system_requirement | approved | All responses contain a X-Content-Type-Options: nosniff header |
| SR-0272 | system_requirement | approved | A Strict-Transport-Security header is included on all responses and for all subdomains |
| SR-0273 | system_requirement | approved | A suitable Referrer-Policy header is included to avoid exposing sensitive information in the URL |
| SR-0274 | system_requirement | approved | The content of a web application cannot be embedded in a third-party site by default and that |
| SR-0275 | system_requirement | approved | The application server only accepts the HTTP methods in use by the application/API |
| SR-0276 | system_requirement | approved | The supplied Origin header is not used for authentication or access control decisions |
| SR-0277 | system_requirement | approved | The Cross-Origin Resource Sharing (CORS) Access-Control-Allow-Origin header uses a strict allow |
| SR-0278 | system_requirement | approved | HTTP headers added by a trusted proxy or SSO devices |
<!-- tl:end -->

