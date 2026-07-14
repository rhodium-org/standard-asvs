# OWASP ASVS 5.0.0 — throughline source

This document is **generated from the graph** by `tl docs`; `tl docs --check` gates
it in CI. The prose headings are hand-owned — everything between `tl:*` markers is
injected from the YAML items, so the published spec can never drift from the graph.

This source is a faithful, complete cut of **OWASP ASVS v5.0.0**: every chapter is
a `user_requirement`, and every verification requirement is a `system_requirement`
that `implements` its chapter. The published ASVS number lives in `attrs.source_ref`
(e.g. `V1.1.1`); the ASVS level in `attrs.level`. The throughline UIDs are this
source's own and immutable — a consumer cites a clause as `asvs:SR-0001`, never by its
ASVS number.

It carries
<!-- tl:count type == 'user_requirement' -->
17
<!-- tl:end --> chapters and
<!-- tl:count type == 'system_requirement' -->
345
<!-- tl:end --> verification requirements.

## Purpose

<!-- tl:item INT-0001 -->
**INT-0001 — An application's security is verifiable against a graded, testable baseline** — `intent`, status `approved`

> The OWASP Application Security Verification Standard exists so that an application's security controls can be verified against a normative, level-graded set of requirements — giving developers, testers and procurers a shared baseline rather than ad-hoc judgement.

**source_ref**: ASVS 5.0.0
<!-- tl:end -->

## V1 Encoding and Sanitization

<!-- tl:item UR-0001 -->
**UR-0001 — V1 Encoding and Sanitization** — `user_requirement`, status `approved`

> Verification requirements for Encoding and Sanitization (V1).

**source_ref**: V1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V1.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0001 | system_requirement | approved | Input is decoded or unescaped into a canonical form only once |
| SR-0002 | system_requirement | approved | The application performs output encoding and escaping either as a final step before being used by |
| SR-0003 | system_requirement | approved | Output encoding for an HTTP response |
| SR-0004 | system_requirement | approved | When dynamically building URLs |
| SR-0005 | system_requirement | approved | Output encoding or escaping is used when dynamically building JavaScript content (including JSON) |
| SR-0006 | system_requirement | approved | Data selection or database queries (e |
| SR-0007 | system_requirement | approved | The application protects against OS command injection and that operating system calls use |
| SR-0008 | system_requirement | approved | The application protects against LDAP injection vulnerabilities |
| SR-0009 | system_requirement | approved | The application is protected against XPath injection attacks by using query parameterization or |
| SR-0010 | system_requirement | approved | LaTeX processors are configured securely (such as not using the "--shell-escape" flag) and an |
| SR-0011 | system_requirement | approved | The application escapes special characters in regular expressions (typically using a backslash) to |
| SR-0012 | system_requirement | approved | The application is protected against CSV and Formula Injection |
| SR-0013 | system_requirement | approved | All untrusted HTML input from WYSIWYG editors or similar is sanitized using a well-known and secure |
| SR-0014 | system_requirement | approved | The application avoids the use of eval() or other dynamic code execution features such as Spring |
| SR-0015 | system_requirement | approved | Data being passed to a potentially dangerous context is sanitized beforehand to enforce safety |
| SR-0016 | system_requirement | approved | User-supplied Scalable Vector Graphics (SVG) scriptable content is validated or sanitized to |
| SR-0017 | system_requirement | approved | The application sanitizes or disables user-supplied scriptable or expression template language |
| SR-0018 | system_requirement | approved | The application protects against Server-side Request Forgery (SSRF) attacks |
| SR-0019 | system_requirement | approved | The application protects against template injection attacks by not allowing templates to be built |
| SR-0020 | system_requirement | approved | The application appropriately sanitizes untrusted input before use in Java Naming and Directory |
| SR-0021 | system_requirement | approved | The application sanitizes content before it is sent to memcache to prevent injection attacks |
| SR-0022 | system_requirement | approved | Format strings which might resolve in an unexpected or malicious way when used are sanitized before |
| SR-0023 | system_requirement | approved | The application sanitizes user input before passing to mail systems to protect against SMTP or IMAP |
| SR-0024 | system_requirement | approved | Regular expressions are free from elements causing exponential backtracking |
| SR-0025 | system_requirement | approved | The application uses memory-safe string |
| SR-0026 | system_requirement | approved | Sign |
| SR-0027 | system_requirement | approved | Dynamically allocated memory and resources are released |
| SR-0028 | system_requirement | approved | The application configures XML parsers to use a restrictive configuration and that unsafe features |
| SR-0029 | system_requirement | approved | Deserialization of untrusted data enforces safe input handling |
| SR-0030 | system_requirement | approved | Different parsers used in the application for the same data type (e |
<!-- tl:end -->

## V2 Validation and Business Logic

<!-- tl:item UR-0002 -->
**UR-0002 — V2 Validation and Business Logic** — `user_requirement`, status `approved`

> Verification requirements for Validation and Business Logic (V2).

**source_ref**: V2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V2.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0031 | system_requirement | approved | The application's documentation defines input validation rules for how to check the validity of |
| SR-0032 | system_requirement | approved | The application's documentation defines how to validate the logical and contextual consistency of |
| SR-0033 | system_requirement | approved | Expectations for business logic limits and validations are documented |
| SR-0034 | system_requirement | approved | Input is validated to enforce business or functional expectations for that input |
| SR-0035 | system_requirement | approved | The application is designed to enforce input validation at a trusted service layer |
| SR-0036 | system_requirement | approved | The application ensures that combinations of related data items are reasonable according to the |
| SR-0037 | system_requirement | approved | The application will only process business logic flows for the same user in the expected sequential |
| SR-0038 | system_requirement | approved | Business logic limits are implemented per the application's documentation to avoid business logic |
| SR-0039 | system_requirement | approved | Transactions are being used at the business logic level such that either a business logic operation |
| SR-0040 | system_requirement | approved | Business logic level locking mechanisms are used to ensure that limited quantity resources (such as |
| SR-0041 | system_requirement | approved | High-value business logic flows require multi-user approval to prevent unauthorized or accidental |
| SR-0042 | system_requirement | approved | Anti-automation controls are in place to protect against excessive calls to application functions |
| SR-0043 | system_requirement | approved | Business logic flows require realistic human timing |
<!-- tl:end -->

## V3 Web Frontend Security

<!-- tl:item UR-0003 -->
**UR-0003 — V3 Web Frontend Security** — `user_requirement`, status `approved`

> Verification requirements for Web Frontend Security (V3).

**source_ref**: V3
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V3.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0044 | system_requirement | approved | Application documentation states the expected security features that browsers using the application |
| SR-0045 | system_requirement | approved | Security controls are in place to prevent browsers from rendering content or functionality in HTTP |
| SR-0046 | system_requirement | approved | Content intended to be displayed as text |
| SR-0047 | system_requirement | approved | The application avoids DOM clobbering when using client-side JavaScript by employing explicit |
| SR-0048 | system_requirement | approved | Cookies have the 'Secure' attribute set |
| SR-0049 | system_requirement | approved | Each cookie's 'SameSite' attribute value is set according to the purpose of the cookie |
| SR-0050 | system_requirement | approved | Cookies have the '__Host-' prefix for the cookie name unless they are explicitly designed to be |
| SR-0051 | system_requirement | approved | If the value of a cookie is not meant to be accessible to client-side scripts (such as a session |
| SR-0052 | system_requirement | approved | When the application writes a cookie |
| SR-0053 | system_requirement | approved | A Strict-Transport-Security header field is included on all responses to enforce an HTTP Strict |
| SR-0054 | system_requirement | approved | The Cross-Origin Resource Sharing (CORS) Access-Control-Allow-Origin header field is a fixed value |
| SR-0055 | system_requirement | approved | HTTP responses include a Content-Security-Policy response header field which defines directives to |
| SR-0056 | system_requirement | approved | All HTTP responses contain an 'X-Content-Type-Options: nosniff' header field |
| SR-0057 | system_requirement | approved | The application sets a referrer policy to prevent leakage of technically sensitive data to |
| SR-0058 | system_requirement | approved | The web application uses the frame-ancestors directive of the Content-Security-Policy header field |
| SR-0059 | system_requirement | approved | The Content-Security-Policy header field specifies a location to report violations |
| SR-0060 | system_requirement | approved | All HTTP responses that initiate a document rendering (such as responses with Content-Type |
| SR-0061 | system_requirement | approved | That |
| SR-0062 | system_requirement | approved | That |
| SR-0063 | system_requirement | approved | HTTP requests to sensitive functionality use appropriate HTTP methods such as POST |
| SR-0064 | system_requirement | approved | Separate applications are hosted on different hostnames to leverage the restrictions provided by |
| SR-0065 | system_requirement | approved | Messages received by the postMessage interface are discarded if the origin of the message is not |
| SR-0066 | system_requirement | approved | JSONP functionality is not enabled anywhere across the application to avoid Cross-Site Script |
| SR-0067 | system_requirement | approved | Data requiring authorization is not included in script resource responses |
| SR-0068 | system_requirement | approved | Authenticated resources (such as images |
| SR-0069 | system_requirement | approved | Client-side assets |
| SR-0070 | system_requirement | approved | The application only uses client-side technologies which are still supported and considered secure |
| SR-0071 | system_requirement | approved | The application will only automatically redirect the user to a different hostname or domain (which |
| SR-0072 | system_requirement | approved | The application shows a notification when the user is being redirected to a URL outside of the |
| SR-0073 | system_requirement | approved | The application's top-level domain (e |
| SR-0074 | system_requirement | approved | The application behaves as documented (such as warning the user or blocking access) if the browser |
<!-- tl:end -->

## V4 API and Web Service

<!-- tl:item UR-0004 -->
**UR-0004 — V4 API and Web Service** — `user_requirement`, status `approved`

> Verification requirements for API and Web Service (V4).

**source_ref**: V4
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V4.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0075 | system_requirement | approved | Every HTTP response with a message body contains a Content-Type header field that matches the |
| SR-0076 | system_requirement | approved | Only user-facing endpoints (intended for manual web-browser access) automatically redirect from |
| SR-0077 | system_requirement | approved | Any HTTP header field used by the application and set by an intermediary layer |
| SR-0078 | system_requirement | approved | Only HTTP methods that are explicitly supported by the application or its API (including OPTIONS |
| SR-0079 | system_requirement | approved | Per-message digital signatures are used to provide additional assurance on top of transport |
| SR-0080 | system_requirement | approved | All application components (including load balancers |
| SR-0081 | system_requirement | approved | When generating HTTP messages |
| SR-0082 | system_requirement | approved | The application does not send nor accept HTTP/2 or HTTP/3 messages with connection-specific header |
| SR-0083 | system_requirement | approved | The application only accepts HTTP/2 and HTTP/3 requests where the header fields and values do not |
| SR-0084 | system_requirement | approved | That |
| SR-0085 | system_requirement | approved | A query allowlist |
| SR-0086 | system_requirement | approved | GraphQL introspection queries are disabled in the production environment unless the GraphQL API is |
| SR-0087 | system_requirement | approved | WebSocket over TLS (WSS) is used for all WebSocket connections |
| SR-0088 | system_requirement | approved | That |
| SR-0089 | system_requirement | approved | That |
| SR-0090 | system_requirement | approved | Dedicated WebSocket session management tokens are initially obtained or validated through the |
<!-- tl:end -->

## V5 File Handling

<!-- tl:item UR-0005 -->
**UR-0005 — V5 File Handling** — `user_requirement`, status `approved`

> Verification requirements for File Handling (V5).

**source_ref**: V5
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V5.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0091 | system_requirement | approved | The documentation defines the permitted file types |
| SR-0092 | system_requirement | approved | The application will only accept files of a size which it can process without causing a loss of |
| SR-0093 | system_requirement | approved | When the application accepts a file |
| SR-0094 | system_requirement | approved | The application checks compressed files (e |
| SR-0095 | system_requirement | approved | A file size quota and maximum number of files per user are enforced to ensure that a single user |
| SR-0096 | system_requirement | approved | The application does not allow uploading compressed files containing symlinks unless this is |
| SR-0097 | system_requirement | approved | The application rejects uploaded images with a pixel size larger than the maximum allowed |
| SR-0098 | system_requirement | approved | Files uploaded or generated by untrusted input and stored in a public folder |
| SR-0099 | system_requirement | approved | When the application creates file paths for file operations |
| SR-0100 | system_requirement | approved | Server-side file processing |
| SR-0101 | system_requirement | approved | The application validates or ignores user-submitted filenames |
| SR-0102 | system_requirement | approved | File names served (e |
| SR-0103 | system_requirement | approved | Files obtained from untrusted sources are scanned by antivirus scanners to prevent serving of known |
<!-- tl:end -->

## V6 Authentication

<!-- tl:item UR-0006 -->
**UR-0006 — V6 Authentication** — `user_requirement`, status `approved`

> Verification requirements for Authentication (V6).

**source_ref**: V6
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V6.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0104 | system_requirement | approved | Application documentation defines how controls such as rate limiting |
| SR-0105 | system_requirement | approved | A list of context-specific words is documented in order to prevent their use in passwords |
| SR-0106 | system_requirement | approved | That |
| SR-0107 | system_requirement | approved | User set passwords are at least 8 characters in length although a minimum of 15 characters is |
| SR-0108 | system_requirement | approved | Users can change their password |
| SR-0109 | system_requirement | approved | Password change functionality requires the user's current and new password |
| SR-0110 | system_requirement | approved | Passwords submitted during account registration or password change are checked against an available |
| SR-0111 | system_requirement | approved | Passwords of any composition can be used |
| SR-0112 | system_requirement | approved | Password input fields use type=password to mask the entry |
| SR-0113 | system_requirement | approved | "paste" functionality |
| SR-0114 | system_requirement | approved | The application verifies the user's password exactly as received from the user |
| SR-0115 | system_requirement | approved | Passwords of at least 64 characters are permitted |
| SR-0116 | system_requirement | approved | A user's password stays valid until it is discovered to be compromised or the user rotates it |
| SR-0117 | system_requirement | approved | The documented list of context specific words is used to prevent easy to guess passwords being |
| SR-0118 | system_requirement | approved | Passwords submitted during account registration or password changes are checked against a set of |
| SR-0119 | system_requirement | approved | Controls to prevent attacks such as credential stuffing and password brute force are implemented |
| SR-0120 | system_requirement | approved | Default user accounts (e |
| SR-0121 | system_requirement | approved | Either a multi-factor authentication mechanism or a combination of single-factor authentication |
| SR-0122 | system_requirement | approved | That |
| SR-0123 | system_requirement | approved | Users are notified of suspicious authentication attempts (successful or unsuccessful) |
| SR-0124 | system_requirement | approved | Email is not used as either a single-factor or multi-factor authentication mechanism |
| SR-0125 | system_requirement | approved | Users are notified after updates to authentication details |
| SR-0126 | system_requirement | approved | Valid users cannot be deduced from failed authentication challenges |
| SR-0127 | system_requirement | approved | System generated initial passwords or activation codes are securely randomly generated |
| SR-0128 | system_requirement | approved | Password hints or knowledge-based authentication (so-called "secret questions") are not present |
| SR-0129 | system_requirement | approved | A secure process for resetting a forgotten password is implemented |
| SR-0130 | system_requirement | approved | If a multi-factor authentication factor is lost |
| SR-0131 | system_requirement | approved | Renewal instructions for authentication mechanisms which expire are sent with enough time to be |
| SR-0132 | system_requirement | approved | Administrative users can initiate the password reset process for the user |
| SR-0133 | system_requirement | approved | Lookup secrets |
| SR-0134 | system_requirement | approved | That |
| SR-0135 | system_requirement | approved | Lookup secrets |
| SR-0136 | system_requirement | approved | Lookup secrets and out-of-band authentication codes have a minimum of 20 bits of entropy (typically |
| SR-0137 | system_requirement | approved | Out-of-band authentication requests |
| SR-0138 | system_requirement | approved | Any authentication factor (including physical devices) can be revoked in case of theft or other loss |
| SR-0139 | system_requirement | approved | Biometric authentication mechanisms are only used as secondary factors together with either |
| SR-0140 | system_requirement | approved | Time-based one-time passwords (TOTPs) are checked based on a time source from a trusted service and |
| SR-0141 | system_requirement | approved | Authentication mechanisms using the Public Switched Telephone Network (PSTN) to deliver One-time |
| SR-0142 | system_requirement | approved | Out-of-band authentication requests |
| SR-0143 | system_requirement | approved | A code based out-of-band authentication mechanism is protected against brute force attacks by using |
| SR-0144 | system_requirement | approved | That |
| SR-0145 | system_requirement | approved | The certificates used to verify cryptographic authentication assertions are stored in a way |
| SR-0146 | system_requirement | approved | The challenge nonce is at least 64 bits in length |
| SR-0147 | system_requirement | approved | That |
| SR-0148 | system_requirement | approved | The presence and integrity of digital signatures on authentication assertions (for example on JWTs |
| SR-0149 | system_requirement | approved | SAML assertions are uniquely processed and used only once within the validity period to prevent |
| SR-0150 | system_requirement | approved | That |
<!-- tl:end -->

## V7 Session Management

<!-- tl:item UR-0007 -->
**UR-0007 — V7 Session Management** — `user_requirement`, status `approved`

> Verification requirements for Session Management (V7).

**source_ref**: V7
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V7.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0151 | system_requirement | approved | The user's session inactivity timeout and absolute maximum session lifetime are documented |
| SR-0152 | system_requirement | approved | The documentation defines how many concurrent (parallel) sessions are allowed for one account as |
| SR-0153 | system_requirement | approved | All systems that create and manage user sessions as part of a federated identity management |
| SR-0154 | system_requirement | approved | The application performs all session token verification using a trusted |
| SR-0155 | system_requirement | approved | The application uses either self-contained or reference tokens that are dynamically generated for |
| SR-0156 | system_requirement | approved | If reference tokens are used to represent user sessions |
| SR-0157 | system_requirement | approved | The application generates a new session token on user authentication |
| SR-0158 | system_requirement | approved | There is an inactivity timeout such that re-authentication is enforced according to risk analysis |
| SR-0159 | system_requirement | approved | There is an absolute maximum session lifetime such that re-authentication is enforced according to |
| SR-0160 | system_requirement | approved | When session termination is triggered (such as logout or expiration) |
| SR-0161 | system_requirement | approved | The application terminates all active sessions when a user account is disabled or deleted (such as |
| SR-0162 | system_requirement | approved | The application gives the option to terminate all other active sessions after a successful change |
| SR-0163 | system_requirement | approved | All pages that require authentication have easy and visible access to logout functionality |
| SR-0164 | system_requirement | approved | Application administrators are able to terminate active sessions for an individual user or for all |
| SR-0165 | system_requirement | approved | The application requires full re-authentication before allowing modifications to sensitive account |
| SR-0166 | system_requirement | approved | Users are able to view and (having authenticated again with at least one factor) terminate any or |
| SR-0167 | system_requirement | approved | The application requires further authentication with at least one factor or secondary verification |
| SR-0168 | system_requirement | approved | Session lifetime and termination between Relying Parties (RPs) and Identity Providers (IdPs) behave |
| SR-0169 | system_requirement | approved | Creation of a session requires either the user's consent or an explicit action |
<!-- tl:end -->

## V8 Authorization

<!-- tl:item UR-0008 -->
**UR-0008 — V8 Authorization** — `user_requirement`, status `approved`

> Verification requirements for Authorization (V8).

**source_ref**: V8
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V8.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0170 | system_requirement | approved | Authorization documentation defines rules for restricting function-level and data-specific access |
| SR-0171 | system_requirement | approved | Authorization documentation defines rules for field-level access restrictions (both read and write) |
| SR-0172 | system_requirement | approved | The application's documentation defines the environmental and contextual attributes (including but |
| SR-0173 | system_requirement | approved | Authentication and authorization documentation defines how environmental and contextual factors are |
| SR-0174 | system_requirement | approved | The application ensures that function-level access is restricted to consumers with explicit |
| SR-0175 | system_requirement | approved | The application ensures that data-specific access is restricted to consumers with explicit |
| SR-0176 | system_requirement | approved | The application ensures that field-level access is restricted to consumers with explicit |
| SR-0177 | system_requirement | approved | Adaptive security controls based on a consumer's environmental and contextual attributes (such as |
| SR-0178 | system_requirement | approved | The application enforces authorization rules at a trusted service layer and doesn't rely on |
| SR-0179 | system_requirement | approved | Changes to values on which authorization decisions are made are applied immediately |
| SR-0180 | system_requirement | approved | Access to an object is based on the originating subject's (e |
| SR-0181 | system_requirement | approved | Multi-tenant applications use cross-tenant controls to ensure consumer operations will never affect |
| SR-0182 | system_requirement | approved | Access to administrative interfaces incorporates multiple layers of security |
<!-- tl:end -->

## V9 Self-contained Tokens

<!-- tl:item UR-0009 -->
**UR-0009 — V9 Self-contained Tokens** — `user_requirement`, status `approved`

> Verification requirements for Self-contained Tokens (V9).

**source_ref**: V9
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V9.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0183 | system_requirement | approved | Self-contained tokens are validated using their digital signature or MAC to protect against |
| SR-0184 | system_requirement | approved | Only algorithms on an allowlist can be used to create and verify self-contained tokens |
| SR-0185 | system_requirement | approved | Key material that is used to validate self-contained tokens is from trusted pre-configured sources |
| SR-0186 | system_requirement | approved | That |
| SR-0187 | system_requirement | approved | The service receiving a token validates the token to be the correct type and is meant for the |
| SR-0188 | system_requirement | approved | The service only accepts tokens which are intended for use with that service (audience) |
| SR-0189 | system_requirement | approved | That |
<!-- tl:end -->

## V10 OAuth and OIDC

<!-- tl:item UR-0010 -->
**UR-0010 — V10 OAuth and OIDC** — `user_requirement`, status `approved`

> Verification requirements for OAuth and OIDC (V10).

**source_ref**: V10
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V10.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0190 | system_requirement | approved | Tokens are only sent to components that strictly need them |
| SR-0191 | system_requirement | approved | The client only accepts values from the authorization server (such as the authorization code or ID |
| SR-0192 | system_requirement | approved | That |
| SR-0193 | system_requirement | approved | That |
| SR-0194 | system_requirement | approved | The OAuth client only requests the required scopes (or other authorization parameters) in requests |
| SR-0195 | system_requirement | approved | The resource server only accepts access tokens that are intended for use with that service |
| SR-0196 | system_requirement | approved | The resource server enforces authorization decisions based on claims from the access token that |
| SR-0197 | system_requirement | approved | If an access control decision requires identifying a unique user from an access token (JWT or |
| SR-0198 | system_requirement | approved | That |
| SR-0199 | system_requirement | approved | The resource server prevents the use of stolen access tokens or replay of access tokens (from |
| SR-0200 | system_requirement | approved | The authorization server validates redirect URIs based on a client-specific allowlist of |
| SR-0201 | system_requirement | approved | That |
| SR-0202 | system_requirement | approved | The authorization code is short-lived |
| SR-0203 | system_requirement | approved | For a given client |
| SR-0204 | system_requirement | approved | The authorization server mitigates refresh token replay attacks for public clients |
| SR-0205 | system_requirement | approved | That |
| SR-0206 | system_requirement | approved | If the authorization server supports unauthenticated dynamic client registration |
| SR-0207 | system_requirement | approved | Refresh tokens have an absolute expiration |
| SR-0208 | system_requirement | approved | Refresh tokens and reference access tokens can be revoked by an authorized user using the |
| SR-0209 | system_requirement | approved | Confidential client is authenticated for client-to-authorized server backchannel requests such as |
| SR-0210 | system_requirement | approved | The authorization server configuration only assigns the required scopes to the OAuth client |
| SR-0211 | system_requirement | approved | For a given client |
| SR-0212 | system_requirement | approved | Grant type 'code' is always used together with pushed authorization requests (PAR) |
| SR-0213 | system_requirement | approved | The authorization server issues only sender-constrained (Proof-of-Possession) access tokens |
| SR-0214 | system_requirement | approved | That |
| SR-0215 | system_requirement | approved | The client is confidential and the authorization server requires the use of strong client |
| SR-0216 | system_requirement | approved | The client (as the relying party) mitigates ID Token replay attacks |
| SR-0217 | system_requirement | approved | The client uniquely identifies the user from ID Token claims |
| SR-0218 | system_requirement | approved | The client rejects attempts by a malicious authorization server to impersonate another |
| SR-0219 | system_requirement | approved | The client validates that the ID Token is intended to be used for that client (audience) by |
| SR-0220 | system_requirement | approved | That |
| SR-0221 | system_requirement | approved | The OpenID Provider only allows values 'code' |
| SR-0222 | system_requirement | approved | The OpenID Provider mitigates denial of service through forced logout |
| SR-0223 | system_requirement | approved | The authorization server ensures that the user consents to each authorization request |
| SR-0224 | system_requirement | approved | When the authorization server prompts for user consent |
| SR-0225 | system_requirement | approved | The user can review |
<!-- tl:end -->

## V11 Cryptography

<!-- tl:item UR-0011 -->
**UR-0011 — V11 Cryptography** — `user_requirement`, status `approved`

> Verification requirements for Cryptography (V11).

**source_ref**: V11
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V11.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0226 | system_requirement | approved | There is a documented policy for management of cryptographic keys and a cryptographic key lifecycle |
| SR-0227 | system_requirement | approved | A cryptographic inventory is performed |
| SR-0228 | system_requirement | approved | Cryptographic discovery mechanisms are employed to identify all instances of cryptography in the |
| SR-0229 | system_requirement | approved | A cryptographic inventory is maintained |
| SR-0230 | system_requirement | approved | Industry-validated implementations (including libraries and hardware-accelerated implementations) |
| SR-0231 | system_requirement | approved | The application is designed with crypto agility such that random number |
| SR-0232 | system_requirement | approved | All cryptographic primitives utilize a minimum of 128-bits of security based on the algorithm |
| SR-0233 | system_requirement | approved | All cryptographic operations are constant-time |
| SR-0234 | system_requirement | approved | All cryptographic modules fail securely |
| SR-0235 | system_requirement | approved | Insecure block modes (e |
| SR-0236 | system_requirement | approved | Only approved ciphers and modes such as AES with GCM are used |
| SR-0237 | system_requirement | approved | Encrypted data is protected against unauthorized modification preferably by using an approved |
| SR-0238 | system_requirement | approved | Nonces |
| SR-0239 | system_requirement | approved | Any combination of an encryption algorithm and a MAC algorithm is operating in encrypt-then-MAC mode |
| SR-0240 | system_requirement | approved | Only approved hash functions are used for general cryptographic use cases |
| SR-0241 | system_requirement | approved | Passwords are stored using an approved |
| SR-0242 | system_requirement | approved | Hash functions used in digital signatures |
| SR-0243 | system_requirement | approved | The application uses approved key derivation functions with key stretching parameters when deriving |
| SR-0244 | system_requirement | approved | All random numbers and strings which are intended to be non-guessable must be generated using a |
| SR-0245 | system_requirement | approved | The random number generation mechanism in use is designed to work securely |
| SR-0246 | system_requirement | approved | Only approved cryptographic algorithms and modes of operation are used for key generation and |
| SR-0247 | system_requirement | approved | Approved cryptographic algorithms are used for key exchange (such as Diffie-Hellman) with a focus |
| SR-0248 | system_requirement | approved | Full memory encryption is in use that protects sensitive data while it is in use |
| SR-0249 | system_requirement | approved | Data minimization ensures the minimal amount of data is exposed during processing |
<!-- tl:end -->

## V12 Secure Communication

<!-- tl:item UR-0012 -->
**UR-0012 — V12 Secure Communication** — `user_requirement`, status `approved`

> Verification requirements for Secure Communication (V12).

**source_ref**: V12
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V12.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0250 | system_requirement | approved | Only the latest recommended versions of the TLS protocol are enabled |
| SR-0251 | system_requirement | approved | Only recommended cipher suites are enabled |
| SR-0252 | system_requirement | approved | The application validates that mTLS client certificates are trusted before using the certificate |
| SR-0253 | system_requirement | approved | Proper certification revocation |
| SR-0254 | system_requirement | approved | Encrypted Client Hello (ECH) is enabled in the application's TLS settings to prevent exposure of |
| SR-0255 | system_requirement | approved | TLS is used for all connectivity between a client and external facing |
| SR-0256 | system_requirement | approved | External facing services use publicly trusted TLS certificates |
| SR-0257 | system_requirement | approved | An encrypted protocol such as TLS is used for all inbound and outbound connections to and from the |
| SR-0258 | system_requirement | approved | TLS clients validate certificates received before communicating with a TLS server |
| SR-0259 | system_requirement | approved | TLS or another appropriate transport encryption mechanism used for all connectivity between internal |
| SR-0260 | system_requirement | approved | TLS connections between internal services use trusted certificates |
| SR-0261 | system_requirement | approved | Services communicating internally within a system (intra-service communications) use strong |
<!-- tl:end -->

## V13 Configuration

<!-- tl:item UR-0013 -->
**UR-0013 — V13 Configuration** — `user_requirement`, status `approved`

> Verification requirements for Configuration (V13).

**source_ref**: V13
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V13.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0262 | system_requirement | approved | All communication needs for the application are documented |
| SR-0263 | system_requirement | approved | For each service the application uses |
| SR-0264 | system_requirement | approved | The application documentation defines resource‑management strategies for every external system or |
| SR-0265 | system_requirement | approved | The application's documentation defines the secrets that are critical for the security of the |
| SR-0266 | system_requirement | approved | Communications between backend application components that don't support the application's standard |
| SR-0267 | system_requirement | approved | Communications between backend application components |
| SR-0268 | system_requirement | approved | If a credential has to be used for service authentication |
| SR-0269 | system_requirement | approved | An allowlist is used to define the external resources or systems with which the application is |
| SR-0270 | system_requirement | approved | The web or application server is configured with an allowlist of resources or systems to which the |
| SR-0271 | system_requirement | approved | Where the application connects to separate services |
| SR-0272 | system_requirement | approved | A secrets management solution |
| SR-0273 | system_requirement | approved | Access to secret assets adheres to the principle of least privilege |
| SR-0274 | system_requirement | approved | All cryptographic operations are performed using an isolated security module (such as a vault or |
| SR-0275 | system_requirement | approved | Secrets are configured to expire and be rotated based on the application's documentation |
| SR-0276 | system_requirement | approved | The application is deployed either without any source control metadata |
| SR-0277 | system_requirement | approved | Debug modes are disabled for all components in production environments to prevent exposure of |
| SR-0278 | system_requirement | approved | Web servers do not expose directory listings to clients unless explicitly intended |
| SR-0279 | system_requirement | approved | Using the HTTP TRACE method is not supported in production environments |
| SR-0280 | system_requirement | approved | Documentation (such as for internal APIs) and monitoring endpoints are not exposed unless |
| SR-0281 | system_requirement | approved | The application does not expose detailed version information of backend components |
| SR-0282 | system_requirement | approved | The web tier is configured to only serve files with specific file extensions to prevent |
<!-- tl:end -->

## V14 Data Protection

<!-- tl:item UR-0014 -->
**UR-0014 — V14 Data Protection** — `user_requirement`, status `approved`

> Verification requirements for Data Protection (V14).

**source_ref**: V14
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V14.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0283 | system_requirement | approved | All sensitive data created and processed by the application has been identified and classified into |
| SR-0284 | system_requirement | approved | All sensitive data protection levels have a documented set of protection requirements |
| SR-0285 | system_requirement | approved | Sensitive data is only sent to the server in the HTTP message body or header fields |
| SR-0286 | system_requirement | approved | The application prevents sensitive data from being cached in server components |
| SR-0287 | system_requirement | approved | Defined sensitive data is not sent to untrusted parties (e |
| SR-0288 | system_requirement | approved | Controls around sensitive data related to encryption |
| SR-0289 | system_requirement | approved | Caching mechanisms are configured to only cache responses which have the expected content type for |
| SR-0290 | system_requirement | approved | The application only returns the minimum required sensitive data for the application's functionality |
| SR-0291 | system_requirement | approved | Sensitive information is subject to data retention classification |
| SR-0292 | system_requirement | approved | Sensitive information is removed from the metadata of user-submitted files unless storage is |
| SR-0293 | system_requirement | approved | Authenticated data is cleared from client storage |
| SR-0294 | system_requirement | approved | The application sets sufficient anti-caching HTTP response header fields (i |
| SR-0295 | system_requirement | approved | Data stored in browser storage (such as localStorage |
<!-- tl:end -->

## V15 Secure Coding and Architecture

<!-- tl:item UR-0015 -->
**UR-0015 — V15 Secure Coding and Architecture** — `user_requirement`, status `approved`

> Verification requirements for Secure Coding and Architecture (V15).

**source_ref**: V15
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V15.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0296 | system_requirement | approved | Application documentation defines risk based remediation time frames for 3rd party component |
| SR-0297 | system_requirement | approved | An inventory catalog |
| SR-0298 | system_requirement | approved | The application documentation identifies functionality which is time-consuming or resource-demanding |
| SR-0299 | system_requirement | approved | Application documentation highlights third-party libraries which are considered to be "risky |
| SR-0300 | system_requirement | approved | Application documentation highlights parts of the application where "dangerous functionality" is |
| SR-0301 | system_requirement | approved | The application only contains components which have not breached the documented update and |
| SR-0302 | system_requirement | approved | The application has implemented defenses against loss of availability due to functionality which is |
| SR-0303 | system_requirement | approved | The production environment only includes functionality that is required for the application to |
| SR-0304 | system_requirement | approved | Third-party components and all of their transitive dependencies are included from the expected |
| SR-0305 | system_requirement | approved | The application implements additional protections around parts of the application which are |
| SR-0306 | system_requirement | approved | The application only returns the required subset of fields from a data object |
| SR-0307 | system_requirement | approved | Where the application backend makes calls to external URLs |
| SR-0308 | system_requirement | approved | The application has countermeasures to protect against mass assignment attacks by limiting allowed |
| SR-0309 | system_requirement | approved | All proxying and middleware components transfer the user's original IP address correctly using |
| SR-0310 | system_requirement | approved | The application explicitly ensures that variables are of the correct type and performs strict |
| SR-0311 | system_requirement | approved | JavaScript code is written in a way that prevents prototype pollution |
| SR-0312 | system_requirement | approved | The application has defenses against HTTP parameter pollution attacks |
| SR-0313 | system_requirement | approved | Shared objects in multi-threaded code (such as caches |
| SR-0314 | system_requirement | approved | Checks on a resource's state |
| SR-0315 | system_requirement | approved | Locks are used consistently to avoid threads getting stuck |
| SR-0316 | system_requirement | approved | Resource allocation policies prevent thread starvation by ensuring fair access to resources |
<!-- tl:end -->

## V16 Security Logging and Error Handling

<!-- tl:item UR-0016 -->
**UR-0016 — V16 Security Logging and Error Handling** — `user_requirement`, status `approved`

> Verification requirements for Security Logging and Error Handling (V16).

**source_ref**: V16
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V16.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0317 | system_requirement | approved | An inventory exists documenting the logging performed at each layer of the application's technology |
| SR-0318 | system_requirement | approved | Each log entry includes necessary metadata (such as when |
| SR-0319 | system_requirement | approved | Time sources for all logging components are synchronized |
| SR-0320 | system_requirement | approved | The application only stores or broadcasts logs to the files and services that are documented in the |
| SR-0321 | system_requirement | approved | Logs can be read and correlated by the log processor that is in use |
| SR-0322 | system_requirement | approved | When logging sensitive data |
| SR-0323 | system_requirement | approved | All authentication operations are logged |
| SR-0324 | system_requirement | approved | Failed authorization attempts are logged |
| SR-0325 | system_requirement | approved | The application logs the security events that are defined in the documentation and also logs |
| SR-0326 | system_requirement | approved | The application logs unexpected errors and security control failures such as backend TLS failures |
| SR-0327 | system_requirement | approved | All logging components appropriately encode data to prevent log injection |
| SR-0328 | system_requirement | approved | Logs are protected from unauthorized access and cannot be modified |
| SR-0329 | system_requirement | approved | Logs are securely transmitted to a logically separate system for analysis |
| SR-0330 | system_requirement | approved | A generic message is returned to the consumer when an unexpected or security-sensitive error occurs |
| SR-0331 | system_requirement | approved | The application continues to operate securely when external resource access fails |
| SR-0332 | system_requirement | approved | The application fails gracefully and securely |
| SR-0333 | system_requirement | approved | A "last resort" error handler is defined which will catch all unhandled exceptions |
<!-- tl:end -->

## V17 WebRTC

<!-- tl:item UR-0017 -->
**UR-0017 — V17 WebRTC** — `user_requirement`, status `approved`

> Verification requirements for WebRTC (V17).

**source_ref**: V17
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('V17.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0334 | system_requirement | approved | The Traversal Using Relays around NAT (TURN) service only allows access to IP addresses that are |
| SR-0335 | system_requirement | approved | The Traversal Using Relays around NAT (TURN) service is not susceptible to resource exhaustion when |
| SR-0336 | system_requirement | approved | The key for the Datagram Transport Layer Security (DTLS) certificate is managed and protected based |
| SR-0337 | system_requirement | approved | The media server is configured to use and support approved Datagram Transport Layer Security (DTLS) |
| SR-0338 | system_requirement | approved | Secure Real-time Transport Protocol (SRTP) authentication is checked at the media server to prevent |
| SR-0339 | system_requirement | approved | The media server is able to continue processing incoming media traffic when encountering malformed |
| SR-0340 | system_requirement | approved | The media server is able to continue processing incoming media traffic during a flood of Secure |
| SR-0341 | system_requirement | approved | The media server is not susceptible to the "ClientHello" Race Condition vulnerability in Datagram |
| SR-0342 | system_requirement | approved | Any audio or video recording mechanisms associated with the media server are able to continue |
| SR-0343 | system_requirement | approved | The Datagram Transport Layer Security (DTLS) certificate is checked against the Session Description |
| SR-0344 | system_requirement | approved | The signaling server is able to continue processing legitimate incoming signaling messages during a |
| SR-0345 | system_requirement | approved | The signaling server is able to continue processing legitimate signaling messages when encountering |
<!-- tl:end -->

