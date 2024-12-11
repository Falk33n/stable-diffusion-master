<script lang="ts">
	import { cn } from '$utils';
	import type { WithElementRef } from 'bits-ui';
	import type { HTMLAttributes } from 'svelte/elements';

	let {
		ref = $bindable(null),
		class: className,
		children,
		...props
	}: WithElementRef<HTMLAttributes<HTMLDivElement>> = $props();
</script>

<div
	bind:this={ref}
	class={cn(
		'flex flex-col-reverse sm:flex-row sm:justify-end sm:space-x-2',
		className,
	)}
	{...props}
>
	{@render children?.()}
</div>
