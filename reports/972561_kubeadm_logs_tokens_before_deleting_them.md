# kubeadm logs tokens before deleting them

## Report Details
- **Report ID**: 972561
- **URL**: https://hackerone.com/reports/972561
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-09-01T23:15:55.868Z
- **Disclosed**: 2020-11-21T18:04:06.009Z

## Reporter
- **Username**: mlevesquedion
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Report Submission Form

## Summary:
`kubeabdm`'s `delete` command takes as input either a bootstrap token ID, or a full token. Before determining whether the input is just an id or a full token, `kubeadm` logs the input using `klog`. If the deletion fails, the token would remain valid. An attacker who has access to the logs could use it to perform actions that require a bootstrap token, such as creating a cluster or joining nodes to an existing cluster.

## Kubernetes Version:
The vulnerable code is present in kubernetes 1.19. The specific line that contains the call to `klog` was last edited on 2019-03-24.

## Steps To Reproduce:
The vulnerable code is in the `github.com/kubernetes` repository, under `kubernetes/cmd/kubeadm/app/cmd/token.go`, at line `423`. Here is the whole function:
```go
// RunDeleteTokens removes a bootstrap tokens from the server.
func RunDeleteTokens(out io.Writer, client clientset.Interface, tokenIDsOrTokens []string) error {
	for _, tokenIDOrToken := range tokenIDsOrTokens {
		// Assume this is a token id and try to parse it
		tokenID := tokenIDOrToken
		klog.V(1).Infof("[token] parsing token %q", tokenIDOrToken) // POTENTIAL LEAK HERE
		if !bootstraputil.IsValidBootstrapTokenID(tokenIDOrToken) {
			// Okay, the full token with both id and secret was probably passed. Parse it and extract the ID only
			bts, err := kubeadmapiv1beta2.NewBootstrapTokenString(tokenIDOrToken)
			if err != nil {
				return errors.Errorf("given token %q didn't match pattern %q or %q",
					tokenIDOrToken, bootstrapapi.BootstrapTokenIDPattern, bootstrapapi.BootstrapTokenIDPattern)
			}
			tokenID = bts.ID
		}

		tokenSecretName := bootstraputil.BootstrapTokenSecretName(tokenID)
		klog.V(1).Infof("[token] deleting token %q", tokenID)
		if err := client.CoreV1().Secrets(metav1.NamespaceSystem).Delete(context.TODO(), tokenSecretName, metav1.DeleteOptions{}); err != nil {
			return errors.Wrapf(err, "failed to delete bootstrap token %q", tokenID)
		}
		fmt.Fprintf(out, "bootstrap token %q deleted\n", tokenID)
	}
	return nil
}
```

And here's the definition of the kubeadm command that calls that function:
```go
	deleteCmd := &cobra.Command{
		Use:                   "delete [token-value] ...",
		DisableFlagsInUseLine: true,
		Short:                 "Delete bootstrap tokens on the server",
		Long: dedent.Dedent(`
			This command will delete a list of bootstrap tokens for you.

			The [token-value] is the full Token of the form "[a-z0-9]{6}.[a-z0-9]{16}" or the
			Token ID of the form "[a-z0-9]{6}" to delete.
		`),
		RunE: func(tokenCmd *cobra.Command, args []string) error {
			if len(args) < 1 {
				return errors.Errorf("missing subcommand; 'token delete' is missing token of form %q", bootstrapapi.BootstrapTokenIDPattern)
			}
			kubeConfigFile = cmdutil.GetKubeConfigPath(kubeConfigFile)
			client, err := getClientset(kubeConfigFile, dryRun)
			if err != nil {
				return err
			}

			return RunDeleteTokens(out, client, args)
		},
	}
```

## Supporting Material/References:
None.

## Impact

An attacker who obtains a bootstrap token from the logs could use it to authenticate with `kubeadm` and create a new cluster or join nodes to an existing cluster, e.g. to use computing resources. An attacker could also perform other actions using `kubeadm`, e.g. listing or deleting other tokens.

## Attachments
No attachments
