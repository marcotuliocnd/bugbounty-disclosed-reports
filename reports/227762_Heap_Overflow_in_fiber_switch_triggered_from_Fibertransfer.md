# Heap Overflow in fiber_switch triggered from Fiber.transfer

## Report Details
- **Report ID**: 227762
- **URL**: https://hackerone.com/reports/227762
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-05-11T18:53:52.394Z
- **Disclosed**: 2017-05-30T14:37:06.630Z

## Reporter
- **Username**: avisaven
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
It appears as if my recommendations were ignored in the GitHub issue, so I've repeated the issue here.

# PoC

	Fiber.new{}.transfer(
		0,0,0,0,0,0,0,0,0,0,
		0,0,0,0,0,0,0,0,0,0,
		0,0,0,0,0,0,0,0,0,0,
		0,0,0,0,0,0,0,0,0,0,
		0,0,0,0,0,0,0,0,0,0,
		0,0,0,0,0,0,0,0,0,0,
		0,0,0,0,0)

# Explanation
The cause of this is that in mrbgems/mruby-fiber/src/fiber.c the stack Fiber stack is initialized lines 90-96 to a default of 64 (FIBER_STACK_INIT_SIZE), however in fiber_switch lines 191-198, if the Fiber's status is currently MRB_FIBER_CREATED, then it will copy the arguments provided from fiber_transfer irregardless of whether or not there are more arguments than 64 (the PoC doesn't need ~127 arguments, anything 64 or above will work!). The quick fix would be to make sure that theres not more than 64 arguments passed to fiber_transfer.

# Solution

	diff --git a/mrbgems/mruby-fiber/src/fiber.c b/mrbgems/mruby-fiber/src/fiber.c
	index bd1d09d4..2d0fc39a 100644
	--- a/mrbgems/mruby-fiber/src/fiber.c
	+++ b/mrbgems/mruby-fiber/src/fiber.c
	@@ -188,6 +188,9 @@ fiber_switch(mrb_state *mrb, mrb_value self, mrb_int len, const mrb_value *a, mr
	   mrb->c->status = resume ? MRB_FIBER_RESUMED : MRB_FIBER_TRANSFERRED;
	   c->prev = resume ? mrb->c : (c->prev ? c->prev : mrb->root_c);
	   if (c->status == MRB_FIBER_CREATED) {
	+    if (len >= FIBER_STACK_INIT_SIZE) {
	+      mrb_raise(mrb, E_FIBER_ERROR, "too many arguments to fiber");
	+    }
	     mrb_value *b = c->stack+1;
	     mrb_value *e = b + len;

## Attachments
No attachments
