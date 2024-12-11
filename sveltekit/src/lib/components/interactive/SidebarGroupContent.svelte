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
	data-sidebar="group-content"
	class={cn('w-full text-sm', className)}
	{...props}
>
	{@render children?.()}
</div>
