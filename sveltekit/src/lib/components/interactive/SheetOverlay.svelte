<script
	module
	lang="ts"
>
	import { Dialog } from 'bits-ui';

	export const Sheet = Dialog.Root;
	export const SheetClose = Dialog.Close;
	export const SheetTrigger = Dialog.Trigger;
	export const SheetPortal = Dialog.Portal;
</script>

<script lang="ts">
	import { cn } from '$utils';

	let {
		ref = $bindable(null),
		class: className,
		...props
	}: Dialog.OverlayProps = $props();
</script>

<Dialog.Overlay
	bind:ref
	class={cn(
		'data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0  fixed inset-0 z-50 bg-black/80',
		className,
	)}
	{...props}
/>
