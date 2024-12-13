<script lang="ts">
	import { cn } from '$utils';
	import { Dialog, type DialogDescriptionProps } from 'bits-ui';

	let {
		ref = $bindable(null),
		class: className,
		...props
	}: DialogDescriptionProps = $props();
</script>

<Dialog.Description
	bind:ref
	class={cn('text-muted-foreground text-sm', className)}
	{...props}
/>
