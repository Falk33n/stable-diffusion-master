<script lang="ts">
	import { cn } from '$utils';
	import type { WithElementRef, WithoutChildren } from 'bits-ui';
	import type { HTMLAttributes } from 'svelte/elements';

	let {
		ref = $bindable(null),
		'aria-hidden': ariaHidden = true,
		class: className,
		...props
	}: WithoutChildren<WithElementRef<HTMLAttributes<HTMLDivElement>>> = $props();
</script>

<div
	bind:this={ref}
	aria-hidden={ariaHidden}
	class={cn('bg-primary/10 animate-pulse rounded-md', className)}
	{...props}
></div>
