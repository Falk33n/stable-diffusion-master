<script lang="ts">
	import { TooltipProvider } from '$components/feedback';
	import {
		setSidebar,
		SIDEBAR_COOKIE_MAX_AGE,
		SIDEBAR_COOKIE_NAME,
		SIDEBAR_WIDTH,
		SIDEBAR_WIDTH_ICON,
	} from '$components/interactive';
	import { cn } from '$utils';
	import type { WithElementRef } from 'bits-ui';
	import type { HTMLAttributes } from 'svelte/elements';

	let {
		ref = $bindable(null),
		open = $bindable(true),
		onOpenChange = () => {},
		controlledOpen = false,
		class: className,
		style,
		children,
		...props
	}: WithElementRef<HTMLAttributes<HTMLDivElement>> & {
		open?: boolean;
		onOpenChange?: (open: boolean) => void;
		controlledOpen?: boolean;
	} = $props();

	const sidebar = setSidebar({
		open: () => open,
		setOpen: (value: boolean) => {
			if (controlledOpen) {
				onOpenChange(value);
			} else {
				open = value;
				onOpenChange(value);
			}

			document.cookie = `${SIDEBAR_COOKIE_NAME}=${open}; path=/; max-age=${SIDEBAR_COOKIE_MAX_AGE}`;
		},
	});
</script>

<svelte:window onkeydown={sidebar.handleShortcutKeydown} />

<TooltipProvider delayDuration={0}>
	<div
		style="--sidebar-width: {SIDEBAR_WIDTH}; --sidebar-width-icon: {SIDEBAR_WIDTH_ICON}; {style}"
		class={cn(
			'group/sidebar-wrapper has-[[data-variant=inset]]:bg-sidebar flex min-h-svh w-full',
			className,
		)}
		bind:this={ref}
		{...props}
	>
		{@render children?.()}
	</div>
</TooltipProvider>
