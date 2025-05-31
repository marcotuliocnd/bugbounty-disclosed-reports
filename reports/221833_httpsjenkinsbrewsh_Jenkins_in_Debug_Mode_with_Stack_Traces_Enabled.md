# [https://jenkins.brew.sh] Jenkins in Debug Mode with Stack Traces Enabled

## Report Details
- **Report ID**: 221833
- **URL**: https://hackerone.com/reports/221833
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-18T10:18:34.498Z
- **Disclosed**: 2017-04-19T10:22:31.431Z

## Reporter
- **Username**: zephrfish
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: homebrew

## Vulnerability Information
The consultant identified that the affected host is running an instance of Jenkins in debug mode, as a result stack traces are enabled. The affected URL below displays a full strack trace from Jenkins:

Affected URL:
- https://jenkins.brew.sh/adjuncts/3a890183/

## Recommendation

Disable stack traces and ensure the installation is properly locked down, consider following Jenkin's security[ lockdown guide](https://wiki.jenkins-ci.org/display/JENKINS/Securing+Jenkins) to enable efficient security measures 

Stack Trace
---
```
java.lang.StringIndexOutOfBoundsException: String index out of range: 0
	at java.lang.String.charAt(String.java:658)
	at org.kohsuke.stapler.framework.adjunct.AdjunctManager.doDynamic(AdjunctManager.java:158)
	at java.lang.invoke.MethodHandle.invokeWithArguments(MethodHandle.java:599)
	at org.kohsuke.stapler.Function$MethodFunction.invoke(Function.java:343)
	at org.kohsuke.stapler.Function.bindAndInvoke(Function.java:184)
	at org.kohsuke.stapler.Function.bindAndInvokeAndServeResponse(Function.java:117)
	at org.kohsuke.stapler.MetaClass$11.dispatch(MetaClass.java:397)
	at org.kohsuke.stapler.Stapler.tryInvoke(Stapler.java:715)
Caused: javax.servlet.ServletException
	at org.kohsuke.stapler.Stapler.tryInvoke(Stapler.java:765)
	at org.kohsuke.stapler.Stapler.invoke(Stapler.java:845)
	at org.kohsuke.stapler.MetaClass$5.doDispatch(MetaClass.java:248)
	at org.kohsuke.stapler.NameBasedDispatcher.dispatch(NameBasedDispatcher.java:58)
	at org.kohsuke.stapler.Stapler.tryInvoke(Stapler.java:715)
	at org.kohsuke.stapler.Stapler.invoke(Stapler.java:845)
	at org.kohsuke.stapler.Stapler.invoke(Stapler.java:649)
	at org.kohsuke.stapler.Stapler.service(Stapler.java:238)
	at javax.servlet.http.HttpServlet.service(HttpServlet.java:790)
	at org.eclipse.jetty.servlet.ServletHolder.handle(ServletHolder.java:812)
	at org.eclipse.jetty.servlet.ServletHandler$CachedChain.doFilter(ServletHandler.java:1669)
	at hudson.util.PluginServletFilter$1.doFilter(PluginServletFilter.java:135)
	at hudson.util.PluginServletFilter.doFilter(PluginServletFilter.java:126)
	at org.eclipse.jetty.servlet.ServletHandler$CachedChain.doFilter(ServletHandler.java:1652)
	at hudson.security.csrf.CrumbFilter.doFilter(CrumbFilter.java:86)
	at org.eclipse.jetty.servlet.ServletHandler$CachedChain.doFilter(ServletHandler.java:1652)
	at hudson.security.ChainedServletFilter$1.doFilter(ChainedServletFilter.java:84)
	at hudson.security.UnwrapSecurityExceptionFilter.doFilter(UnwrapSecurityExceptionFilter.java:51)
	at hudson.security.ChainedServletFilter$1.doFilter(ChainedServletFilter.java:87)
	at jenkins.security.ExceptionTranslationFilter.doFilter(ExceptionTranslationFilter.java:117)
	at hudson.security.ChainedServletFilter$1.doFilter(ChainedServletFilter.java:87)
	at org.acegisecurity.providers.anonymous.AnonymousProcessingFilter.doFilter(AnonymousProcessingFilter.java:125)
	at hudson.security.ChainedServletFilter$1.doFilter(ChainedServletFilter.java:87)
	at org.acegisecurity.ui.rememberme.RememberMeProcessingFilter.doFilter(RememberMeProcessingFilter.java:142)
	at hudson.security.ChainedServletFilter$1.doFilter(ChainedServletFilter.java:87)
	at org.acegisecurity.ui.AbstractProcessingFilter.doFilter(AbstractProcessingFilter.java:271)
	at hudson.security.ChainedServletFilter$1.doFilter(ChainedServletFilter.java:87)
	at jenkins.security.BasicHeaderProcessor.doFilter(BasicHeaderProcessor.java:93)
	at hudson.security.ChainedServletFilter$1.doFilter(ChainedServletFilter.java:87)
	at org.acegisecurity.context.HttpSessionContextIntegrationFilter.doFilter(HttpSessionContextIntegrationFilter.java:249)
	at hudson.security.HttpSessionContextIntegrationFilter2.doFilter(HttpSessionContextIntegrationFilter2.java:67)
	at hudson.security.ChainedServletFilter$1.doFilter(ChainedServletFilter.java:87)
	at hudson.security.ChainedServletFilter.doFilter(ChainedServletFilter.java:76)
	at hudson.security.HudsonFilter.doFilter(HudsonFilter.java:171)
	at org.eclipse.jetty.servlet.ServletHandler$CachedChain.doFilter(ServletHandler.java:1652)
	at org.kohsuke.stapler.compression.CompressionFilter.doFilter(CompressionFilter.java:49)
	at org.eclipse.jetty.servlet.ServletHandler$CachedChain.doFilter(ServletHandler.java:1652)
	at hudson.util.CharacterEncodingFilter.doFilter(CharacterEncodingFilter.java:82)
	at org.eclipse.jetty.servlet.ServletHandler$CachedChain.doFilter(ServletHandler.java:1652)
	at org.kohsuke.stapler.DiagnosticThreadNameFilter.doFilter(DiagnosticThreadNameFilter.java:30)
	at org.eclipse.jetty.servlet.ServletHandler$CachedChain.doFilter(ServletHandler.java:1652)
	at org.eclipse.jetty.servlet.ServletHandler.doHandle(ServletHandler.java:585)
	at org.eclipse.jetty.server.handler.ScopedHandler.handle(ScopedHandler.java:143)
	at org.eclipse.jetty.security.SecurityHandler.handle(SecurityHandler.java:553)
	at org.eclipse.jetty.server.session.SessionHandler.doHandle(SessionHandler.java:223)
	at org.eclipse.jetty.server.handler.ContextHandler.doHandle(ContextHandler.java:1127)
	at org.eclipse.jetty.servlet.ServletHandler.doScope(ServletHandler.java:515)
	at org.eclipse.jetty.server.session.SessionHandler.doScope(SessionHandler.java:185)
	at org.eclipse.jetty.server.handler.ContextHandler.doScope(ContextHandler.java:1061)
	at org.eclipse.jetty.server.handler.ScopedHandler.handle(ScopedHandler.java:141)
	at org.eclipse.jetty.server.handler.HandlerWrapper.handle(HandlerWrapper.java:97)
	at org.eclipse.jetty.server.Server.handle(Server.java:499)
	at org.eclipse.jetty.server.HttpChannel.handle(HttpChannel.java:311)
	at org.eclipse.jetty.server.HttpConnection.onFillable(HttpConnection.java:257)
	at org.eclipse.jetty.io.AbstractConnection$2.run(AbstractConnection.java:544)
	at winstone.BoundedExecutorService$1.run(BoundedExecutorService.java:77)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1145)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:615)
	at java.lang.Thread.run(Thread.java:745)

```

## Attachments
No attachments
