<script lang="ts">
	import { cn } from '$utils';
	import { Separator, type SeparatorRootProps } from 'bits-ui';

	let {
		ref = $bindable(null),
		class: className,
		'aria-hidden': ariaHidden = true,
		orientation = 'horizontal',
		...props
	}: SeparatorRootProps = $props();
</script>

<Separator.Root
	bind:ref
	aria-hidden={ariaHidden}
	class={cn(
		'bg-border shrink-0',
		orientation === 'horizontal' ? 'h-[1px] w-full' : 'min-h-full w-[1px]',
		className,
	)}
	{orientation}
	{...props}
/>
