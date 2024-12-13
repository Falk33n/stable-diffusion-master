<script lang="ts">
	import { Button } from '$components/forms';
	import { useSidebar } from '$components/interactive';
	import { cn } from '$utils';
	import { PanelLeft } from 'lucide-svelte/icons';
	import type { ComponentProps } from 'svelte';

	let {
		ref = $bindable(null),
		class: className,
		onclick,
		...props
	}: ComponentProps<typeof Button> & {
		onclick?: (e: MouseEvent) => void;
	} = $props();

	const sidebar = useSidebar();
</script>

<Button
	type="button"
	onclick={(e) => {
		onclick?.(e);
		sidebar.toggle();
	}}
	data-sidebar="trigger"
	variant="ghost"
	size="icon"
	aria-label="Toggle Sidebar"
	class={cn('size-7', className)}
	{...props}
>
	<PanelLeft aria-hidden />
</Button>
