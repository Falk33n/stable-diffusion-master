<script lang="ts">
	import { cn } from '$utils';
	import type { WithElementRef } from 'bits-ui';
	import type { HTMLAttributes } from 'svelte/elements';

	let {
		ref = $bindable(null),
		class: className,
		children,
		...props
	}: WithElementRef<
		HTMLAttributes<HTMLUListElement>,
		HTMLUListElement
	> = $props();
</script>

<ul
	bind:this={ref}
	data-sidebar="menu"
	class={cn('flex w-full min-w-0 flex-col gap-1', className)}
	{...props}
>
	{@render children?.()}
</ul>
