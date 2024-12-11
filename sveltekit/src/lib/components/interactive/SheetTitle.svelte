<script lang="ts">
	import { cn } from '$utils';
	import { Dialog, type DialogTitleProps } from 'bits-ui';

	let {
		ref = $bindable(null),
		class: className,
		...props
	}: DialogTitleProps = $props();
</script>

<Dialog.Title
	bind:ref
	class={cn('text-foreground text-lg font-semibold', className)}
	{...props}
/>
